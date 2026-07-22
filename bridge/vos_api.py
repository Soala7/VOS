"""
File: VOS/bridge/vos_api.py

VOS API Bridge

Provides access to VOS services for external systems
such as the C shell.
"""


class VOSAPI:

    def __init__(self):

        self.filesystem = None
        self.process_manager = None
        self.window_manager = None


    # -------------------------
    # Service registration
    # -------------------------

    def register_filesystem(self, filesystem):

        self.filesystem = filesystem


    def register_process_manager(self, process_manager):

        self.process_manager = process_manager


    def register_window_manager(self, window_manager):

        self.window_manager = window_manager



    # -------------------------
    # Filesystem commands
    # -------------------------

    def pwd(self):

        if self.filesystem:

            return self.filesystem.get_current_path()

        return "/"



    def ls(self, path=None):

        if not self.filesystem:

            return ""


        try:

            if path is None or path == "":

                contents = (
                    self.filesystem.current_directory
                    .list_contents()
                )
                print(
                    "[VOS API] ls contents:",
                    contents
                )

            else:

                contents = (
                    self.filesystem.list_directory(path)
                )


            if contents is None:

                return ""


            # New filesystem format:
            # {
            #     "folders": [],
            #     "files": []
            # }

            if isinstance(contents, dict):

                folders = contents.get(
                    "folders",
                    []
                )

                files = contents.get(
                    "files",
                    []
                )

                return "\n".join(
                    folders + files
                )


            # Old list format

            if isinstance(contents, list):

                return "\n".join(contents)


        except Exception as error:

            print(
                "[VOS API] ls error:",
                error
            )


        return ""



    def cd(self, path):

        if not self.filesystem:

            return False


        print(
            "[VOS API] cd request:",
            path
        )


        try:

            success = (
                self.filesystem
                .change_directory(path)
            )


            print(
                "[VOS API] cd result:",
                success
            )


            return success


        except Exception as error:

            print(
                "[VOS API] cd error:",
                error
            )

            return False



    def mkdir(self, path):

        if not self.filesystem:

            return False


        print(
            "[VOS API] mkdir request:",
            path
        )


        try:

            success = (
                self.filesystem
                .create_folder(path)
            )


            print(
                "[VOS API] mkdir result:",
                success
            )


            return success


        except Exception as error:

            print(
                "[VOS API] mkdir error:",
                error
            )

            return False



    def touch(self, path):

        if not self.filesystem:

            return False


        print(
            "[VOS API] touch request:",
            path
        )


        try:

            success = (
                self.filesystem
                .create_file(path)
            )


            print(
                "[VOS API] touch result:",
                success
            )


            return success


        except Exception as error:

            print(
                "[VOS API] touch error:",
                error
            )

            return False



# Global API instance

vos_api = VOSAPI()