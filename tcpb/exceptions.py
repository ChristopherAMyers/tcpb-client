"""Exception handling for tcpb package

See https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions
"""

class TCPBError(Exception):
    """Base error for package
    """
    pass

class ServerError(TCPBError):
    """Raised when socket connection to server dies

    Pulls logfile out of scratch dir for convenience
    """
    def __init__(self, msg, client):
        msg += '\n\nServer Address: {}\n'.format(client.tcaddr)

        job_dir = client.curr_job_dir
        job_id = client.curr_job_id
        if job_dir is not None and job_id is not None:
            logfile = '{}/{}.log'.format(job_dir, job_id)
            with open(logfile, 'r') as logf:
                lines = logf.readlines()
            
            debuglines = ''.join(lines[-10:])
            msg += 'Last 10 lines from logfile ({}):\n{}'.format(logfile, debuglines)
        else:
            msg += 'No current running job found, could not parse logfile'

        super(ServerError, self).__init__(msg)
