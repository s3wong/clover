// Copyright (c) Authors of Clover
//
// All rights reserved. This program and the accompanying materials
// are made available under the terms of the Apache License, Version 2.0
// which accompanies this distribution, and is available at
// http://www.apache.org/licenses/LICENSE-2.0

package cmd

import (
    "fmt"
    "gopkg.in/resty.v1"
    "github.com/spf13/cobra"
)


var startidsCmd = &cobra.Command{
    Use:   "ids",
    Short: "Start IDS process",
    Long: `Restart IDS process when adding custom rules`,
    Run: func(cmd *cobra.Command, args []string) {
        startIDS()
    },
}

func init() {
    startCmd.AddCommand(startidsCmd)
}

func startIDS() {

    url := controllerIP + "/snort/start"

    resp, err := resty.R().
    Get(url)
    if err != nil {
        panic(err.Error())
    }
    fmt.Printf("\n%v\n", resp)
}


