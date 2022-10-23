package goutil

import (
	"strings"
)

const TestCaseNameSep = "RIO_"

// GetTestCaseShortName -
func GetTestCaseShortName(caseName string) string {
	results := strings.Split(caseName, TestCaseNameSep)
	if len(results) < 2 {
		return caseName
	}

	return results[len(results)-1]
}

// IsCaseSkipped - return true/false to determine if the skip case list contains this case by case method name
func IsCaseSkipped(caseName string, caseList string) bool {
	return IsCaseInList(caseName, caseList)
}

// IsCaseInList -
func IsCaseInList(caseName, caseList string) bool {
	if strings.TrimSpace(caseName) == "" || strings.TrimSpace(caseList) == "" {
		return false
	}

	shortName := GetTestCaseShortName(caseName)
	for _, caseName := range strings.Split(caseList, ",") {
		if strings.TrimSpace(caseName) == shortName {
			return true
		}
	}
	return false
}

// ReduceContents -
func ReduceContents(raw string, filter []string) string {
	newContents := make([]string, 0)
	contents := strings.Split(raw, "\n")
	for _, c := range contents {
		if !containSub(c, filter) {
			newContents = append(newContents, c)
		}
	}

	return strings.Join(newContents, "\n")
}

func containSub(s string, subS []string) bool {
	c := false
	for _, sub := range subS {
		if strings.Contains(s, sub) {
			return true
		}
	}
	return c
}
