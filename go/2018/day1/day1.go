package main

import (
	"fmt"
	"os"

	"../../common"
)

func part1(inputx interface{}, sum int) {
	freqs := make(map[int]bool)
	switch t := inputx.(type) {
	case []int:
		for {
			for _, val := range t {
				sum += val
				_, ok := freqs[sum]
				if ok {
					fmt.Printf("repeated:%d\n", sum)
					os.Exit(0)
				}
				freqs[sum] = true
			}
			fmt.Printf("sum = %d\n", sum)
		}
	}
}

func main() {
	ir := &common.InputReader{
		Filename:      "input.txt",
		TypeToConvert: "int",
	}
	x, _ := ir.ReadPuzzleInput()
	part1(x, 0)
}
