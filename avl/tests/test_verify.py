from avl import verify
import os
from os.path import dirname, realpath


def test_verreport(tmp_path):
    data_path = realpath(os.path.join(dirname(realpath(__file__)),
                         '../../data-samples'))
    dataset_list = list(map(lambda f: os.path.join(data_path, f),
                            os.listdir(data_path)))

    list_path = os.path.join(tmp_path, 'datasets.txt')
    with open(list_path, 'w') as fh:
        for dataset in dataset_list:
            fh.write(dataset + '\n')

    report = verify.make_report(list_path)
    expected = '| Dataset | Result |\n|----|----|\n' + ''.join(
        [f'| `{ds}` | PASS |\n' for ds in dataset_list]
    )
    assert expected == report
