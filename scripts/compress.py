import argparse
import re


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str, help='file to compile and insert requires')
    parser.add_argument('target', type=str, help='results')
    return parser.parse_args()


def compile_file(fname):
    loc = []
    with open(fname, 'r') as source_file:
        for line in source_file:
            m = re.match(r'include\(([a-zA-Z0-9-_]+)\)', line)
            if line.startswith('--') and len(loc) > 2: # keep title
                continue
            if m:
                loc += compile_file(m.group(1) + '.lua')
                continue
            loc.append(line.strip())
    return loc

if __name__ == "__main__":
    args = parse_args()
    loc = compile_file(args.source)
    with open(args.target, 'w') as target_file:
        target_file.write('\n'.join(loc))
