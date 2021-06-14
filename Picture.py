#!/usr/bin/env python3
import numpy as np
#
#  +------------------+ B
#  |                  |
#  |                  |
#  |                  |
#  |                  |
#  +------------------+
#  A
#
#  sqr: xA, yA, xB, yB
#
nput = [[  0,  0,  3,  4 ],
        [ -1, -1,  2,  1 ],
        [  4,  1,  7,  5 ],
        [  3,  0,  8,  2 ]]

def CONFIG( xmin, ymax, a ):
    ''' Coverse Factory '''
    def converse( sqr ):
        """ square to array """
        for y in range( sqr[1], sqr[3] ):
            for x in range( sqr[0], sqr[2] ):
                i = ymax - y
                j = x - xmin + 1
                a[ i, j ] = 1
    return converse

def dfs( a ):
    """"""
    z = np.zeros( a.shape, dtype=int ) # vi[z]ited
    c = 0 # perimeter counter
    #    E         S         W          N
    w = ( 0, 1 ), ( 1, 0 ), ( 0, -1 ), ( -1, 0 )

    def explore( i, j ):
        nonlocal c
        z[ i, j ] = 1 # mark as visited
        for di, dj in w:
            m = i + di
            n = j + dj
            if a[ m, n ] == 1 and z[ m, n ] == 0:
                explore( m, n )
            if a[ m, n ] == 0 and z[ m, n ] == 0:
                z[ m, n ] = 1
                c += 1

    for ( i, j ), e in np.ndenumerate( a ):
        if e == 1 and z[ i, j ] == 0:
            explore( i, j )

    return c
    
def main():
    """ voom """
    # get min/max ranges
    xmin = min( nput, key = lambda e: e[0])[0]
    xmax = max( nput, key = lambda e: e[2])[2]
    ymin = min( nput, key = lambda e: e[1])[1]
    ymax = max( nput, key = lambda e: e[3])[3]
    wid = xmax - xmin # width
    ght = ymax - ymin # height
    # create array with a frame
    a = np.zeros(( ght + 2, wid + 2 ), dtype=int )
    converse = CONFIG( xmin, ymax, a )
    for sqr in nput: converse( sqr )
    c = dfs( a )
    print( a )
    print( "Perimeter:", c )

if __name__ == '__main__': main()

# log: - Insult is like a whip on the back of a slave.
