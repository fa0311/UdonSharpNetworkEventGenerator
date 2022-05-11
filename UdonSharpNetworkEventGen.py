import argparse


argpar = argparse.ArgumentParser(
    prog="UdonSharpNetworkEventGen",
    usage="https://github.com/fa0311/UdonSharpNetworkEventGen",
    description="UdonSharp NetworkEvent Generator",
)

argpar.add_argument("name")
argpar.add_argument("range", type=int)
argpar.add_argument("-o", "--output", default="Output.cs")
argpar.add_argument("--indent", default="    ")
argpar.add_argument("--crlf", default="\n")

arg = argpar.parse_args()



output = ""
for i in range(arg.range):
    output += "public void NetworkEvent{name}{number}(){{{crlf}"\
        "{indent}NetworkEvent{name}({number});{crlf}"\
        "}}{crlf}".format(name=arg.name,number=i, indent=arg.indent, crlf=arg.crlf)

with open(arg.output, mode='w') as f:
    f.write(output)