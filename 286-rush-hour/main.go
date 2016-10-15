package main

import (
	"os"

	"github.com/Sirupsen/logrus"
	prefixed "github.com/x-cray/logrus-prefixed-formatter"
)

var log = logrus.New()

func init() {
	log.Formatter = new(prefixed.TextFormatter)
	log.Level = logrus.DebugLevel
}

func main() {
	if len(os.Args) != 2 {
		log.Fatal("must provide a puzzle file")
	}

	board := Read(os.Args[1])
	board.Print()
}
