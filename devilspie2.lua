-- the debug_print command does only print anything to stdout
-- if devilspie2 is run using the --debug option
debug_print("Window Name: " .. get_window_name());
debug_print("Application name: " .. get_application_name())

if (get_application_name() == "Rhythmbox") or (get_application_name() == "Signal Private Messenger") or (get_application_name() == "emacs")then
   pin_window();
end

if (get_application_name() == "Thunderbird") or (get_application_name() == "Shotwell") then
   set_window_workspace(1);
end
