import asyncio
from revoltutils import Config

async def main():
    config = Config(app_name="TestTool")

    # Ensure config directory is created
    print("[+] Config directory:", config.config_dir)

    # Create a test config file
    config_name = "test-config.yaml"
    default_data = {"api_key": "123456", "enabled": True}
    created_path = await config.create_config_file(filename=config_name, content=default_data, overwrite=True)
    print(f"[+] Created config: {created_path}")

    # Read the config back
    data = await config.read_config(filename=config_name)
    print("[+] Read config:", data)

    # Modify and write config
    data["enabled"] = False
    await config.write_config(data, filename=config_name)
    print("[+] Modified and wrote config.")

    # Read again to confirm changes
    updated = await config.read_config(filename=config_name)
    print("[+] Updated config:", updated)

    # List all YAML configs
    all_configs = config.list_configs()
    print("[+] All config files:", [str(f.name) for f in all_configs])

    # Ensure config (should not recreate)
    ensured_path = await config.ensure_config(filename=config_name)
    print("[+] Ensured config exists:", ensured_path)

    # Delete the test config
    deleted = config.delete_config(config_name)
    print(f"[+] Deleted config {config_name}: {deleted}")

    # Confirm deletion
    still_exists = config.config_exists(config_name)
    print("[+] Config exists after delete:", still_exists)

if __name__ == "__main__":
    asyncio.run(main())
