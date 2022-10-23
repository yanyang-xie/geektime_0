package goutil

import (
	"github.comcast.com/viper-cog/goutil/assert"
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
		assert.Equals(t, tc.want, GetTestCaseShortName(tc.caseName))
	}
}

func TestIsCaseInList(t *testing.T) {
	type testCase struct {
		caseName string
		caseList string
		want     bool
	}

	testCases := []testCase{
		// contain "RIO_"
		{"TestArchivedAfterConfiguredTimeRIO_RCCS_AA_TC1", "RCCS_AA_TC1,RCCS_AA_TC2", true},
		// not contain "RIO_"
		{"TestArchivedAfterConfiguredTime_RCCS_AA_TC1", "RCCS_AA_TC1,RCCS_AA_TC2", false},
		// contain multiple "RIO_"
		{"TestArchivedAfterConfiguredTime_RIO_RCCS_AA_TC1_RIO_AA_Test2", "RCCS_AA_TC1,RCCS_AA_TC2,AA_Test2,RCCS_AA_TC3,RCCS_AA_TC5", true},
	}

	for _, tc := range testCases {
		assert.Equals(t, tc.want, IsCaseInList(tc.caseName, tc.caseList))
	}
}
