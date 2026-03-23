// start paused time in a idk how?
input.onButtonPressed(Button.A, function () {
    timer_started = true
    basic.showString("started timer")
    while (timer != 0) {
        basic.pause(1000)
        timer += -1
        if (time == 1) {
            time_data = 15
        } else if (time == 2) {
            time_data = 30
        } else if (time == 3) {
            time_data = 60
        } else if (time == 4) {
            time_data = 120
        } else if (time == 5) {
            time_data = paused_time / 60
        } else {
            continue;
        }
        serial.writeLine("" + (light_level))
        serial.writeLine("" + (sound_level))
        serial.writeLine("" + (time_data))
    }
})
input.onButtonPressed(Button.AB, function () {
    critical_state = false
    timer_started = false
    time = 0
    pause2 = true
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    paused_time = timer
    basic.showString("timer paused!")
    basic.showString("press A to restart timer")
    while (timer_started == false) {
        basic.showLeds(`
            . . # . .
            . # . # .
            # . . . #
            # # # # #
            # . . . #
            `)
        basic.pause(200)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.pause(200)
    }
})
input.onGesture(Gesture.Shake, function () {
    time += 1
    if (time == 1) {
        timer = 900
        basic.showNumber(1)
    } else if (time == 2) {
        timer = 1800
        basic.showNumber(2)
    } else if (time == 3) {
        timer = 3600
        basic.showNumber(3)
    } else if (time == 4) {
        timer = 7200
        basic.showNumber(4)
    } else {
        time = 0
        basic.showNumber(0)
    }
})
let paused_time = 0
let timer_started = false
let pause2 = false
let critical_state = false
let time_data = 0
let timer = 0
let time = 0
let sound_level = 0
let light_level = 0
serial.redirectToUSB()
serial.setBaudRate(BaudRate.BaudRate115200)
light_level = input.lightLevel()
sound_level = input.soundLevel()
time = 0
timer = 0
time_data = 0
critical_state = false
let too_loud = false
let too_bright = false
let too_dark = false
pause2 = false
basic.forever(function () {
    if (timer_started == true) {
        light_level = input.lightLevel()
        sound_level = input.soundLevel()
        if (light_level > 200) {
            too_bright = true
            while (too_bright == true) {
                critical_state = true
                basic.showLeds(`
                    # . # . #
                    . # # # .
                    # # . # #
                    . # # # .
                    # . # . #
                    `)
                basic.pause(100)
                basic.showLeds(`
                    . . . . .
                    . # # # .
                    . # . # .
                    . # # # .
                    . . . . .
                    `)
                basic.pause(100)
                basic.showLeds(`
                    . . . . .
                    . . . . .
                    . . # . .
                    . . . . .
                    . . . . .
                    `)
                basic.pause(100)
                too_bright = false
                light_level = input.lightLevel()
                critical_state = false
                if (light_level > 200) {
                    too_bright = true
                }
            }
        } else if (light_level < 30) {
            too_dark = true
            while (too_dark == true) {
                critical_state = true
                basic.showLeds(`
                    . . . . .
                    . . . . .
                    . . # . .
                    . . . . .
                    . . . . .
                    `)
                basic.pause(100)
                basic.showLeds(`
                    . . . . .
                    . # # # .
                    . # . # .
                    . # # # .
                    . . . . .
                    `)
                basic.pause(100)
                basic.showLeds(`
                    # . # . #
                    . # # # .
                    # # . # #
                    . # # # .
                    # . # . #
                    `)
                basic.pause(100)
                too_dark = false
                light_level = input.lightLevel()
                critical_state = false
                if (light_level < 50) {
                    too_dark = true
                }
            }
        } else if (sound_level >= 200) {
            basic.pause(2000)
            if (sound_level >= 200) {
                too_loud = true
                while (too_loud == true) {
                    critical_state = true
                    basic.showLeds(`
                        . . # . .
                        . . # # .
                        . . # . #
                        # # # . .
                        # # # . .
                        `)
                    basic.pause(100)
                    basic.showLeds(`
                        . # # # .
                        . # # # .
                        # # # # #
                        . # # # .
                        . . # . .
                        `)
                    basic.pause(100)
                    too_loud = false
                    sound_level = input.soundLevel()
                    critical_state = false
                    if (sound_level > 200) {
                        too_dark = true
                    }
                }
            }
        } else {
            basic.clearScreen()
        }
    }
})
basic.forever(function () {
    while (critical_state == true) {
        if (pause2 == true) {
            basic.pause(60000)
            pause2 = false
        }
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
        music.rest(music.beat(BeatFraction.Quarter))
        music.play(music.tonePlayable(392, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
        music.rest(music.beat(BeatFraction.Quarter))
    }
})
