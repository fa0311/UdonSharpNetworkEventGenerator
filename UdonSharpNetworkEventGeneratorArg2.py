import argparse


argpar = argparse.ArgumentParser(
    prog="UdonSharpNetworkEventGenerator",
    usage="https://github.com/fa0311/UdonSharpNetworkEventGenerator",
    description="UdonSharp NetworkEvent Generator",
)

argpar.add_argument("name")
argpar.add_argument("range", type=int)
argpar.add_argument("range2", type=int)
argpar.add_argument("-o", "--output", default="Output.cs")
argpar.add_argument("--indent", default="    ")
argpar.add_argument("--crlf", default="\n")

arg = argpar.parse_args()



output = ""
for i in range(arg.range):
    for ii in range(arg.range2):
        output += "public void NetworkEvent{name}{number}_{number2}(){{{crlf}"\
            "{indent}NetworkEvent{name}({number},{number2});{crlf}"\
            "}}{crlf}".format(name=arg.name, number=i, number2=ii, indent=arg.indent, crlf=arg.crlf)

with open(arg.output, mode='w') as f:
    f.write(output)