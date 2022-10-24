package goutil

import (
	"testing"
)

func TestGetTestCaseShortName(t *testing.T) {
	type testCase struct {
		caseName string
		want     string
	}

	testCases := []testCase{
		// contain "RIO_"
		{"TestArchivedAfterConfiguredTimeRIO_RCCS_AA_TC1", "RCCS_AA_TC1"},
		// not contain "RIO_"
		{"", ""},
		{"TestArchivedAfterConfiguredTime_RCCS_AA_TC1", "TestArchivedAfterConfiguredTime_RCCS_AA_TC1"},
		// contain multiple "RIO_"
		{"TestArchivedAfterConfiguredTime_RIO_RCCS_AA_TC1_RIO_AA_Test2", "AA_Test2"},
	}

	for _, tc := range testCases {
		if tc.want != GetTestCaseShortName(tc.caseName) {
			t.Fatalf("fail to validate test case short name. want: %v, got: %v", tc.want, GetTestCaseShortName(tc.caseName))
		}
	}
}

