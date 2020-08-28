import contextlib
import threading
import time

import discord_rpc


@contextlib.contextmanager
def with_discord_rich_presence(opencity, state):
    print('test')

    def _with_discord_rich_presence():
        def readyCallback(current_user):
            print('Our user: {}'.format(current_user))

        def disconnectedCallback(codeno, codemsg):
            print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
                codeno, codemsg
            ))

        def errorCallback(errno, errmsg):
            print('An error occurred! Error {}: {}'.format(
                errno, errmsg
            ))

        # Note: 'event_name': callback
        callbacks = {
            'ready': readyCallback,
            'disconnected': disconnectedCallback,
            'error': errorCallback,
        }
        print('initing')
        discord_rpc.initialize('651420362940088336', callbacks=callbacks, log=True)
        start = time.time()
        print('moving to while loop')
        print('in while loop')
        while True:
            discord_rpc.update_presence(
                **{
                    'state': state,
                    'details': "City Simulation",
                    'start_timestamp': start,
                    'large_image_key': 'opencityicon',
                    'large_image_text': '{}'.format(f'{opencity.Name} v{opencity.Version}'),
                    'small_image_key': 'spar_games',
                    'small_image_text': 'Made by SPAR Interactive'
                }
            )

            discord_rpc.update_connection()
            time.sleep(5)
            discord_rpc.run_callbacks()

    thread = threading.Thread(target=_with_discord_rich_presence)
    thread.start()
    yield True
    thread.join()
    discord_rpc.shutdown()
