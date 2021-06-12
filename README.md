# Webpage to Telegraph Adapter

Adapter library to [Export to Telegraph](https://github.com/gaoyunzhi/export_to_telegraph): Transfer webpage to
Telegraph archive.  
hacking with monkey patches.

## Usage

```
import webpage2telegraph
webpage2telegraph.token = YOUR_TELEGRAPH_TOKEN
telegraph_url = webpage2telegraph.transfer(webpage_url)
```

If transfer failed, `telegraph_url` will be `None`.

## Install

```
pip3 install webpage2telegraph
```