package main

import (
	"fmt"
	"strconv"
)

type bitfield int64

func (f bitfield) Binary() string {
	return fmt.Sprintf("%036s", strconv.FormatInt(int64(f), 2))
}

// PrintGrid prints out a grid of bytes givne the expected size in column
func PrintGrid(b []byte, cols int) {
	offset := 0
	total := len(b)
	tmp := []byte{}
	for {
		tmp = append(tmp, b[offset:offset+6]...)
		tmp = append(tmp, '\n')
		offset += cols
		if offset == total {
			break
		}
	}
	fmt.Println(string(tmp))
}
