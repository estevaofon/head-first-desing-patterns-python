from abc import abstractmethod, ABC


class Light:
    def __init__(self, name):
        self.name = name

    def on(self):
        print(self.name + ' light is on')

    def off(self):
        print(self.name + ' light is off')


class CeilingFan:
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0

    def __init__(self, name):
        self.name = name
        self.speed = self.OFF

    def high(self):
        self.speed = self.HIGH
        print(self.name + ' ceiling fan is on high')

    def medium(self):
        self.speed = self.MEDIUM
        print(self.name + ' ceiling fan is on medium')

    def low(self):
        self.speed = self.LOW
        print(self.name + ' ceiling fan is on low')

    def off(self):
        self.speed = self.OFF
        print(self.name + ' ceiling fan is off')

    def get_speed(self):
        return self.speed


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class CeilingFanHighCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = None

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.high()

    def undo(self):
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()


class RemoteControlWithUndo:
    def __init__(self):
        self.on_commands = []
        self.off_commands = []
        self.undo_command = None

    def set_command(self, slot, on_command, off_command):
        self.on_commands.insert(slot, on_command)
        self.off_commands.insert(slot, off_command)

    def on_button_was_pushed(self, slot):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_was_pushed(self, slot):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_was_pushed(self):
        self.undo_command.undo()

    def __str__(self):
        string_buff = ['\n------ Remote Control -------\n']
        for i in range(len(self.on_commands)):
            string_buff.append('[slot ' + str(i) + '] ' + self.on_commands[i].__class__.__name__ + '    ' + self.off_commands[i].__class__.__name__ + '\n')
        string_buff.append('[undo] ' + self.undo_command.__class__.__name__ + '\n')
        return ''.join(string_buff)


class RemoteLoader:
    def __init__(self):
        self.remote_control = RemoteControlWithUndo()

    def run(self):
        living_room_light = Light('Living Room')
        kitchen_light = Light('Kitchen')
        ceiling_fan = CeilingFan('Living Room Ceiling Fan')

        living_room_light_on = LightOnCommand(living_room_light)
        living_room_light_off = LightOffCommand(living_room_light)
        kitchen_light_on = LightOnCommand(kitchen_light)
        kitchen_light_off = LightOffCommand(kitchen_light)

        ceiling_fan_high = CeilingFanHighCommand(ceiling_fan)

        self.remote_control.set_command(0, living_room_light_on, living_room_light_off)
        self.remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
        self.remote_control.set_command(2, ceiling_fan_high, ceiling_fan.off)

        print(self.remote_control)
        self.remote_control.on_button_was_pushed(0)
        self.remote_control.off_button_was_pushed(0)

        print(self.remote_control)
        self.remote_control.undo_button_was_pushed()
        self.remote_control.on_button_was_pushed(2)


if __name__ == '__main__':
    remote_loader = RemoteLoader()
    remote_loader.run()

