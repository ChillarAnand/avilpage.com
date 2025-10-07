<!--
.. title: Use Space As Both Space & Control - Avoid Emacs Pinky!
.. slug: use-space-as-both-space-control-avoid
.. date: 2014-08-29 17:27:00
.. category: programming
.. tags: emacs, ubuntu, macbook
.. description: How to bind space bar to Control or any other modifier key in Ubuntu or Mac or Windows.
.. link:
.. type: text
-->


Most of the  commands  in  Emacs start with  'Control' & 'Meta'. Control key is present at the corners of the keyboard, and it's very uncomfortable to press it every-time to invoke a command. Most popular solution to this is to swap CAPS lock & CTRL key. But you have to press the key with Pinky which might cause Emacs Pinky.

A much better solution is to use space bar as control key. When you press the space bar, it will function as a normal space key. If you press it with any other key. it will function as control key. So, to run any commands, you can hold space with one thumb and press other key(s) with another hand which will be handy.

In Linux, we can achieve this with Space2Ctrl.

Install the dependencies, clone the repo, make and start the script.

```sh 
sudo apt-get install libx11-dev libxtst-dev

git clone https://github.com/r0adrunner/Space2Ctrl

cd Space2Ctrl

make

./s2cctl start
```

Now you can use your space as space and control key.

If you are using Mac, you can use [Karabiner](https://pqrs.org/osx/karabiner/){target="_blank"} with the following modification.

```json
{
  "title": "Change spacebar to spacebar & control",
  "rules": [
    {
      "description": "SpaceControl",
      "manipulators": [
        {
          "from": {
            "key_code": "spacebar",
            "modifiers": {
              "optional": [
                "any"
              ]
            }
          },
          "to": [
            {
              "key_code": "right_control"
            }
          ],
          "to_if_alone": [
            {
              "key_code": "spacebar"
            }
          ],
          "type": "basic"
        }
      ]
    }
  ]
}
```
