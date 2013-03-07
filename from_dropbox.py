import os
import os.path


import platform
platform.install()


import from_csv


if __name__ == '__main__':

    root = '/home/edmund/Dropbox/ed and matt'

    print '** contents of dropbox/input:'
    for fn in os.listdir(os.path.join(*([root, 'input']))):
        if fn.endswith('.csv'):
            print fn

    while True:
        base_fn = raw_input('which file? > ')
        fn = os.path.join(*([root, 'input', base_fn]))
        if os.path.isfile(fn):
            break
        print '"%s" aint no file I ever heard of' % fn

    out_dir = '.'.join(base_fn.split('.')[:-1])
    platform.Platform.set_root(os.path.join(*([root, 'output', out_dir])))

    from_csv.run(fn)
