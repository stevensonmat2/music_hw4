import argparse
from synth import Synth

parser = argparse.ArgumentParser()
parser.add_argument("--root", type=int, default=48)
parser.add_argument("--beats", type=int, default=8)
parser.add_argument("--bpm", type=float, default=90.0)
parser.add_argument("--ramp", type=float, default=0.5)
parser.add_argument("--accent", type=float, default=5)
parser.add_argument("--volume", type=float, default=8)
args = parser.parse_args()


def main():
    synth = Synth(args)
    synth.play_sequence()


if __name__ == "__main__":
    main()
