test = ['LowQual', 'VQSRTranche']

check = 'VQSRTrancheSNP99.90to100.00'
check = 'VQSRTrancheSNP99.90to100.00'


print not any(substring in check for substring in test)

print not any([False, False, False])