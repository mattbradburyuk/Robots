# Variable list

#  script variables/ constants

# Constants
LEFT = 0
RIGHT = 1
MIN = 0
MAX = 1

DEBUG = True

ADCTIME = 0.001

## Tic toc constants
TICTOC_START = 0
TICTOC_COUNT = 0
TICTOC_MEAN = 0
TICTOC_MAX = -float('inf')
TICTOC_MIN = float('inf')

## Encoder buffer constants and variables
ENC_BUF_SIZE = 2**9
ENC_IND = [0, 0]
ENC_TIME = [[0]*ENC_BUF_SIZE, [0]*ENC_BUF_SIZE]
ENC_VAL = [[0]*ENC_BUF_SIZE, [0]*ENC_BUF_SIZE]

ADC_LOCK = threading.Lock()

## Run variables
RUN_FLAG = True
RUN_FLAG_LOCK = threading.Lock()


# Quickbot class properties

 # Parameters
    sampleTime = 20.0 / 1000.0

    # Pins
    ledPin = 'USR1'

    # Motor Pins -- (LEFT, RIGHT)
    dir1Pin = ('P8_14', 'P8_12')
    dir2Pin = ('P8_16', 'P8_10')
    pwmPin = ('P9_16', 'P9_14')

    # ADC Pins
    irPin = ('P9_38', 'P9_40', 'P9_36', 'P9_35', 'P9_33')
    encoderPin = ('P9_39', 'P9_37')

    # Encoder counting parameter and variables
    ticksPerTurn = 16  # Number of ticks on encoder disc
    encWinSize = 2**5  # Should be power of 2
    minPWMThreshold = [45, 45]  # Threshold on the minimum value to turn wheel
    encTPrev = [0.0, 0.0]
    encThreshold = [0.0, 0.0]
    encTickState = [0, 0]
    encTickStateVec = np.zeros((2, encWinSize))

    # Constraints
    pwmLimits = [-100, 100]  # [min, max]

    # State PWM -- (LEFT, RIGHT)
    pwm = [0, 0]

    # State IR
    irVal = [0.0, 0.0, 0.0, 0.0, 0.0]
    ithIR = 0

    # State Encoder
    encTime = [0.0, 0.0]  # Last time encoders were read
    encPos = [0.0, 0.0]  # Last encoder tick position
    encVel = [0.0, 0.0]  # Last encoder tick velocity

    # Encoder counting parameters
    encCnt = 0  # Count of number times encoders have been read
    encSumN = [0, 0]  # Sum of total encoder samples
    encBufInd0 = [0, 0]  # Index of beginning of new samples in buffer
    encBufInd1 = [0, 0]  # Index of end of new samples in buffer
    encTimeWin = np.zeros((2, encWinSize))  # Moving window of encoder sample times
    encValWin = np.zeros((2, encWinSize))  # Moving window of encoder raw sample values
    encPWMWin = np.zeros((2, encWinSize))  # Moving window corresponding PWM input values
    encTau = [0.0, 0.0]  # Average sampling time of encoders

    ## Stats of encoder values while input = 0 and vel = 0
    encZeroCntMin = 2**4  # Min number of recorded values to start calculating stats
    encZeroMean = [0.0, 0.0]
    encZeroVar = [0.0, 0.0]
    encZeroCnt = [0, 0]
    encHighCnt = [0, 0]
    encLowCnt = [0, 0]
    encLowCntMin = 2

    # Variables
    ledFlag = True
    cmdBuffer = ''

    # UDP
    baseIP = '192.168.7.1'
    robotIP = '192.168.7.2'
    port = 5005
    robotSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    robotSocket.setblocking(False)


# QuickBot class Debug properties

            ## Stats of encoder values while moving -- high, low, and all tick state
            self.encHighLowCntMin = 2**5  # Min number of recorded values to start calculating stats
            self.encHighMean = [0.0, 0.0]
            self.encHighVar = [0.0, 0.0]
            self.encHighTotalCnt = [0, 0]
        
            self.encLowMean = [0.0, 0.0]
            self.encLowVar = [0.0, 0.0]
            self.encLowTotalCnt = [0, 0]
        
            self.encNonZeroCntMin = 2**5
            self.encNonZeroMean = [0.0, 0.0]
            self.encNonZeroVar = [0.0, 0.0]
            self.encNonZeroCnt = [0, 0]

            # Record variables
            self.encRecSize = 2**13
            self.encRecInd = [0, 0]
            self.encTimeRec = np.zeros((2, self.encRecSize))
            self.encValRec = np.zeros((2, self.encRecSize))
            self.encPWMRec = np.zeros((2, self.encRecSize))
            self.encNNewRec = np.zeros((2, self.encRecSize))
            self.encPosRec = np.zeros((2, self.encRecSize))
            self.encVelRec = np.zeros((2, self.encRecSize))
            self.encTickStateRec = np.zeros((2, self.encRecSize))
            self.encThresholdRec = np.zeros((2, self.encRecSize))


# output.txt columns

self.encTimeRec[LEFT], 
self.encValRec[LEFT], 
self.encPWMRec[LEFT], 
self.encNNewRec[LEFT],
self.encTickStateRec[LEFT], 
self.encPosRec[LEFT], 
self.encVelRec[LEFT], 
self.encThresholdRec[LEFT], 

self.encTimeRec[RIGHT], 
self.encValRec[RIGHT], 
self.encPWMRec[RIGHT], 
self.encNNewRec[RIGHT], 
self.encTickStateRec[RIGHT], 
self.encPosRec[RIGHT], 
self.encVelRec[RIGHT], 
self.encThresholdRec[RIGHT]



