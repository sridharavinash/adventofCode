package common

import (
	"bufio"
	"errors"
	"os"
	"strconv"
)

//InputReader struct to hold the file params
type InputReader struct {
	scanner       *bufio.Scanner
	Filename      string
	TypeToConvert string
}

//ReadPuzzleInput -reads the file as scanner and returns an array of converted data
func (ir InputReader) ReadPuzzleInput() (interface{}, error) {
	f, _ := os.Open(ir.Filename)
	ir.scanner = bufio.NewScanner(f)

	switch ir.TypeToConvert {
	case "int":
		ret := make([]int, 0)
		for ir.scanner.Scan() {
			val, _ := strconv.Atoi(ir.scanner.Text())
			ret = append(ret, val)
		}
		return ret, nil
	case "default":
		return nil, errors.New("Not Implemented")
	}
	return nil, errors.New("BOOM")
}
