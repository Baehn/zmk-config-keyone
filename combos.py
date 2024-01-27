text = """
        combo_NUM1 {
            timeout-ms = <50>;
            key-positions = <0 NUM1>;
            bindings = <&kp KEY>;
            layers = <1>
        };
"""

for i, x in enumerate(range(14, 32)):
    out = text.replace("NUM1", f"{x}")
    out = out.replace("KEY", chr(i+65))
    print(out)
