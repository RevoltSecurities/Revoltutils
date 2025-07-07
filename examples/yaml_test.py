import asyncio
import os
from revoltutils import YamlUtils

TEST_FILE = "test_config.yaml"

TEST_DATA = {
    "name": "Revolt",
    "tools": ["nmap", "ffuf"],
    "agents": ["Agent1:Recon", "Agent2:Exploit"]
}


async def setup_test_file():
    await YamlUtils.write_yaml(TEST_FILE, TEST_DATA)


async def test_read_yaml():
    data = await YamlUtils.read_yaml(TEST_FILE)
    assert data["name"] == "Revolt"
    print("[✓] read_yaml passed")


async def test_write_yaml():
    new_data = {"version": "1.0"}
    await YamlUtils.write_yaml(TEST_FILE, new_data, overwrite=False)
    data = await YamlUtils.read_yaml(TEST_FILE)
    assert data["version"] == "1.0"
    assert data["name"] == "Revolt"
    print("[✓] write_yaml passed")


async def test_get_set_value():
    await YamlUtils.set_value(TEST_FILE, "category", "pentest")
    val = await YamlUtils.get_value(TEST_FILE, "category")
    assert val == "pentest"
    print("[✓] get_value / set_value passed")


async def test_delete_key():
    success = await YamlUtils.delete_key(TEST_FILE, "category")
    assert success
    val = await YamlUtils.get_value(TEST_FILE, "category")
    assert val is None
    print("[✓] delete_key passed")


async def test_get_all_keys():
    keys = await YamlUtils.get_all_keys(TEST_FILE)
    assert "name" in keys and "tools" in keys
    print("[✓] get_all_keys passed")


async def test_custom_key_value():
    result = await YamlUtils.custom_key_value(TEST_FILE)
    assert "tools" in result
    assert result["tools"] == ["nmap", "ffuf"]
    print("[✓] custom_key_value passed")


async def test_dual_key_value():
    result = await YamlUtils.dual_key_value(TEST_FILE)
    assert result == [("agents", "Agent1", "Recon"), ("agents", "Agent2", "Exploit")]
    print("[✓] dual_key_value passed")


async def test_get_nested():
    nested_yaml = {
        "config": {
            "user": {
                "name": "admin",
                "role": "root"
            }
        }
    }
    await YamlUtils.write_yaml(TEST_FILE, nested_yaml)
    val = await YamlUtils.get_nested(TEST_FILE, ["config", "user", "role"])
    assert val == "root"
    print("[✓] get_nested passed")


async def cleanup():
    try:
        os.remove(TEST_FILE)
    except Exception:
        pass


async def main():
    await setup_test_file()
    await test_read_yaml()
    await test_write_yaml()
    await test_get_set_value()
    await test_delete_key()
    await test_get_all_keys()
    await test_custom_key_value()
    await test_dual_key_value()
    await test_get_nested()
    await cleanup()
    print("\n[*] All YamlUtils tests passed successfully.")


if __name__ == "__main__":
    asyncio.run(main())
