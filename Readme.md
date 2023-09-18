# Handle multiple Chrome profile instance using thread  
```
1. git clone https://github.com/piriyaraj/chrome-profiles-in-multithread.git
2. cd chrome-profiles-in-multithread
3. python -m venv venv
4. venv\Scripts\activate
5. pip install -r requirements.txt
```
go to 
venv\Lib\site-packages\undetected_chromedriver\patcher.py

you can see a function called unzip_package as below
```
    def unzip_package(self, fp):
        """
        Does what it says

        :return: path to unpacked executable
        """
        exe_path = self.exe_name
        if not self.is_old_chromedriver:
            # The new chromedriver unzips into its own folder
            zip_name = f"chromedriver-{self.platform_name}"
            exe_path = os.path.join(zip_name, self.exe_name)

        logger.debug("unzipping %s" % fp)
        try:
            os.unlink(self.zip_path)
        except (FileNotFoundError, OSError):
            pass

        os.makedirs(self.zip_path, mode=0o755, exist_ok=True)
        with zipfile.ZipFile(fp, mode="r") as zf:
            zf.extractall(self.zip_path)
        os.rename(os.path.join(self.zip_path, exe_path), self.executable_path)
        os.remove(fp)
        shutil.rmtree(self.zip_path)
        os.chmod(self.executable_path, 0o755)
        return self.executable_path
```

change it as

```
    def unzip_package(self, fp):
        """
        Does what it says

        :return: path to unpacked executable
        """
        exe_path = self.exe_name
        if not self.is_old_chromedriver:
            # The new chromedriver unzips into its own folder
            zip_name = f"chromedriver-{self.platform_name}"
            exe_path = os.path.join(zip_name, self.exe_name)

        logger.debug("unzipping %s" % fp)
        try:
            os.unlink(self.zip_path)
        except (FileNotFoundError, OSError):
            pass

        os.makedirs(self.zip_path, mode=0o755, exist_ok=True)
        with zipfile.ZipFile(fp, mode="r") as zf:
            zf.extractall(self.zip_path)
        try:
            os.rename(os.path.join(self.zip_path, exe_path), self.executable_path)
            os.remove(fp)
            shutil.rmtree(self.zip_path)
        except:
            pass
        os.chmod(self.executable_path, 0o755)
        return self.executable_path
```

run ```python main.py```

It will open the 3 new profile and save it in a folder called profiles for using next execution.

in the main.py you can add new profiles as much as you want.
every profile works in same time

your can use it for
```
Parallel Execution: Run multiple Chrome profiles simultaneously for efficiency.
Isolation: Keep profiles independent for separate tasks or configurations.
Resource Efficiency: Minimize resource usage by using threads instead of processes.
Easy Management: Simplify profile management and customization in main.py.
Profile Persistence: Save profiles for reuse in future executions.
Customization: Customize each profile with extensions and settings.
Debugging and Monitoring: Monitor and debug issues more effectively.
Scalability: Scale the number of profiles to meet your needs.
```