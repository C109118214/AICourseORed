import numpy as np
R_pi = np.pi / 180
print( R_pi )

D = np.array( [ 30, 45, 60, 90, 180, 270 ] )
for i in range ( len( D ) ):
    value = np.sin( D[ i ] * R_pi )
    print( "%s%3d%s = %5.2f" % ( "sin", D[ i ], "度的三角函數值", value ) )

#180度轉換弧度是3.1416
print( np.deg2rad( 180 ) )
#弧度pi除以2是90度
print( np.rad2deg( np.pi / 2 ) )
#sin根號2除以2的反函數值的度
Rad = np.arcsin( np.sqrt( 2 ) / 2 )
print( Rad )

print( np.rad2deg( Rad ) )
#cos根號3除以2的反函數值的度
Rad = np.arccos( np.sqrt( 3 ) / 2 )
print( Rad )
print( np.rad2deg( Rad ) )
#tan根號3反函數值的度
Rad = np.arctan( np.sqrt( 3 ) )
print( Rad )

print( np.rad2deg( Rad ) )

Part_A = np.sin( 30 * R_pi ) + np.tan( 45 * R_pi )
Part_B = 1 - np.sin( 45 * R_pi ) + np.cos( 60 * R_pi )
print( Part_A, Part_B )

print( np.round( Part_A * Part_B, 4 ) )

Part_C = ( np.sin( R_pi / 3 ) ** 2 ) + np.sin( R_pi / 6 ) ** 2
Part_D = 1 + np.tan( R_pi / 4 ) + np.cos( R_pi / 3 )
print( Part_C, Part_D )

print( np.round( Part_C * Part_D, 4 ) )