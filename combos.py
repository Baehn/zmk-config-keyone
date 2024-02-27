text = """
        combo_NUM1 {
            timeout-ms = <50>;
            key-positions = <0 NUM1>;
            bindings = <&kp KEY>;
        };
"""

for i, x in enumerate(range(1, 32)):
    out = text.replace("NUM1", f"{x}")
    out = out.replace("KEY", chr((i % 26)+65))
    print(out)
