#! /usr/bin/env python
"""
Flushes the cached docs for next CircleCI build.
"""
import os
from datetime import datetime as dt


def update_cache_timestamp(timestamp_filename):
    """ Updates the contents of the docs-cache-timestamp file
    with current timestamp.

    Returns
    -------
    None
    """
    timestamp_dirpath = os.path.dirname(__file__)
    timestamp_filepath = os.path.join(timestamp_dirpath, timestamp_filename)
    utc_now_timestamp = dt.utcnow()
    with open(timestamp_filepath, 'w') as write_obj:
        write_obj.write(str(utc_now_timestamp))


def get_cache_to_be_cleared(valid_options, cli_args):
    if len(cli_args) == 1:
        cache_to_be_cleared = input(
                'Enter which cache to be cleared. '
                'Valid options are {}: '.format(valid_options)
                )
    else:
        cache_to_be_cleared = cli_args[1]
    return cache_to_be_cleared


def clear_cache(valid_options, which_cache):
    if which_cache == 'docs':
        update_cache_timestamp('docs-cache-timestamp')
    elif which_cache == 'packages':
        update_cache_timestamp('packages-cache-timestamp')
    elif which_cache == 'both':
        update_cache_timestamp('docs-cache-timestamp')
        update_cache_timestamp('packages-cache-timestamp')
    else:
        err_msg = ('Invalid option. '
                   'Valid options are: {}. '
                   'You entered: {}'
                   ).format(valid_options, which_cache)
        raise ValueError(err_msg)


def main():
    cli_args = os.sys.argv
    valid_options = ('docs', 'packages', 'both')
    which_cache = get_cache_to_be_cleared(valid_options=valid_options,
                                          cli_args=cli_args,
                                          )
    clear_cache(valid_options=valid_options,
                which_cache=which_cache,
                )


if __name__ == '__main__':
    main()
