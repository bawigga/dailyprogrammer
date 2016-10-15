package main

import (
	"bufio"
	"bytes"
	"os"
	"strings"

	"github.com/Sirupsen/logrus"
)

// Board wrapper for RushHour board
type Board struct {
	positions map[string]bitfield
	origin    string
}

func (b Board) Print() {
	log := log.WithFields(logrus.Fields{"prefix": "board"})
	viewBoard := bytes.Repeat([]byte("."), 36)
	for i := range b.positions {
		log.Debugf("processing: %s", string(i))

		idx := 0
		bitmap := b.positions[i]

		for {
			if bitmap > 0 {
				if bitmap&1 > 0 {
					log.Infof("setting %s on idx %d", i, idx)
					copy(viewBoard[idx:], []byte(i))
				}

				bitmap = bitmap >> 1
				idx++
			} else {
				break
			}
		}

	}
	PrintGrid(viewBoard, 6)
}

// Read reads in a board from a file
func Read(fileName string) (b Board) {
	log.Debugf("opening %s", fileName)
	f, _ := os.Open(fileName)
	br := bufio.NewReader(f)

	b.positions = make(map[string]bitfield)

	lineNum := 0
	idx := 0 // bitfield index
	for {

		line, err := br.ReadString('\n')
		if err != nil {
			break
		}

		line = strings.TrimSpace(line)

		for _, c := range line {
			vehicleID := string(c)
			if vehicleID != "." {
				b.positions[vehicleID] = b.positions[vehicleID] | (1 << uint8(idx))
			}
			idx++
		}
		lineNum++
	}
	return
}
