def test_benign_lfi_demo():
    print("=== LFI PoC START ===")
    with open("/etc/hosts", "r") as f:
        data = f.read()
    print(data[:1000])  # cap output
    print("=== LFI PoC END ===")
    assert True
