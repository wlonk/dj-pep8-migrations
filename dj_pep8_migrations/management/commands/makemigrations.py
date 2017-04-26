import os

import autopep8

from django.core.management.commands import makemigrations

from django.db.migrations.writer import MigrationWriter


class Command(makemigrations.Command):
    def pep8ify(self, string):
        # AutoPEP8 doesn't actually work well enough, but it's a first
        # step:
        return autopep8.fix_code(string, options={'aggressive': 1})

    def write_migration_files(self, changes):
        """
        Take a changes dict and write them out as migration files.
        """
        directory_created = {}
        for app_label, app_migrations in changes.items():
            if self.verbosity >= 1:
                self.stdout.write(
                    self.style.MIGRATE_HEADING(
                        "Migrations for '%s':" % app_label
                    ) + "\n"
                )
            for migration in app_migrations:
                # Describe the migration
                writer = MigrationWriter(migration)
                if self.verbosity >= 1:
                    # Display a relative path if it's below the current
                    # working directory, or an absolute path otherwise.
                    try:
                        migration_string = os.path.relpath(writer.path)
                    except ValueError:
                        migration_string = writer.path
                    if migration_string.startswith('..'):
                        migration_string = writer.path
                    self.stdout.write(
                        "  %s\n" % (
                            self.style.MIGRATE_LABEL(migration_string),
                        )
                    )
                    for operation in migration.operations:
                        self.stdout.write("    - %s\n" % operation.describe())
                self.actually_write_file(writer, app_label, directory_created)

    # Split this out from write_migration_files to get the mccabe
    # complexity checker to stop complaining:
    def actually_write_file(self, writer, app_label, directory_created):
        if not self.dry_run:
            # Write the migrations file to the disk.
            migrations_directory = os.path.dirname(writer.path)
            if not directory_created.get(app_label):
                if not os.path.isdir(migrations_directory):
                    os.mkdir(migrations_directory)
                init_path = os.path.join(
                    migrations_directory, "__init__.py",
                )
                if not os.path.isfile(init_path):
                    open(init_path, "w").close()
                # We just do this once per app
                directory_created[app_label] = True
            migration_string = self.pep8ify(writer.as_string())
            with open(writer.path, "w", encoding='utf-8') as fh:
                fh.write(migration_string)
        elif self.verbosity == 3:
            # Alternatively, makemigrations --dry-run --verbosity 3 will
            # output the migrations to stdout rather than saving the
            # file to the disk.
            self.stdout.write(
                self.style.MIGRATE_HEADING(
                    "Full migrations file '%s':" % writer.filename
                ) + "\n"
            )
            self.stdout.write("%s\n" % writer.as_string())
