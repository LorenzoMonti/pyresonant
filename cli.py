
def cli(parser):
    parser.add_argument("--input", required=False, type=int, help="Audio Input Device")
    parser.add_argument("--volthresh", required=False, type=float, help="Set the Volume Threshold")
    parser.add_argument("--mapping", required=False, help="Map notes with keys with this pattern: note-key,note-key")
    parser.add_argument("--mappingcsv", required=False, help="Add the path of the csv with this pattern: note,key")
    args = parser.parse_args()
    return args
