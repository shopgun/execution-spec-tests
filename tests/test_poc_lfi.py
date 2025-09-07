def test_benign_lfi_demo():
    data = open("/etc/hosts").read()[:800]
    print("=== LFI PoC START ==="); print(data); print("=== LFI PoC END ===")
    assert False, "Intentional fail to surface captured output"
