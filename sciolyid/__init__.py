import sciolyid.config as config

def setup(**kwargs):
    required = config.required.keys()
    optional = config.optional.keys()
    id_required = config.id_required.keys()

    for option in required:
        try:
            config.options[option] = kwargs[option]
        except KeyError:
            raise config.BotConfigError(f"Required setup argument {option}")

    for option in optional:
        try:
            config.options[option] = kwargs[option]
        except KeyError:
            continue

    if config.options["id_groups"]:
        for option in id_required:
            try:
                config.options[option] = kwargs[option]
            except KeyError:
                raise config.BotConfigError(f"Required setup argument {option} when id_groups is True")

    if config.options['file_folder'] and not config.options['file_folder'].endswith("/"):
        config.options['file_folder'] += "/"

    if config.options['data_dir'] and not config.options['data_dir'].endswith("/"):
        config.options['data_dir'] += "/"

    if config.options['backups_dir'] and not config.options['backups_dir'].endswith("/"):
        config.options['backups_dir'] += "/"

    if config.options['download_dir'] and not config.options['download_dir'].endswith("/"):
        config.options['download_dir'] += "/"

    if config.options['list_dir'] and not config.options['list_dir'].endswith("/"):
        config.options['list_dir'] += "/"

    if config.options['restricted_list_dir'] and not config.options['restricted_list_dir'].endswith("/"):
        config.options['restricted_list_dir'] += "/"

    if config.options['log_dir'] and not config.options['log_dir'].endswith("/"):
        config.options['log_dir'] += "/"

    config.options["log_dir"] = f"{config.options['file_folder']}{config.options['log_dir']}"
    config.options["download_dir"] = f"{config.options['file_folder']}{config.options['download_dir']}"
    config.options["backups_dir"] = f"{config.options['file_folder']}{config.options['backups_dir']}"

    config.options["list_dir"] = f"{config.options['data_dir']}{config.options['list_dir']}"
    config.options["restricted_list_dir"] = f"{config.options['data_dir']}{config.options['restricted_list_dir']}"
    config.options["wikipedia_file"] = f"{config.options['data_dir']}{config.options['wikipedia_file']}"
    config.options["alias_file"] = f"{config.options['data_dir']}{config.options['alias_file']}"

    config.options["id_type"] = config.options["id_type"].lower()
    config.options["category_name"] = config.options["category_name"].title()

    config.options["short_id_type"] = config.options["short_id_type"] or config.options["id_type"][0]

def start():
    import sciolyid.start_bot  # pylint: disable=unused-import
