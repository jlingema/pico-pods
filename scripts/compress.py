import argparse
import re
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str, help='file to compile and insert requires')
    parser.add_argument('target', type=str, help='results')
    return parser.parse_args()


def compile_file(fname):
    loc = []
    with open(fname, 'r') as source_file:
        for i, line in enumerate(source_file):
            line = line.strip()  # remove indentation
            m = re.match(r'include\(([a-zA-Z0-9-_/]+)\)', line)  # includes
            if line.startswith('--') and len(loc) > 2: # keep title
                continue
            if m:
                include_fname = m.group(1) + '.lua'
                if not os.path.isfile(include_fname):
                    print('Cannot find file for inclusion:', include_fname)
                    print('       included in', fname, 'line', i+1)
                    sys.exit(1)
                loc += compile_file(include_fname)
                continue
            loc.append()
    return loc

if __name__ == "__main__":
    args = parse_args()
    loc = compile_file(args.source)
    with open(args.target, 'w') as target_file:
        target_file.write('\n'.join(loc))
