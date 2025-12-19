---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.ServerManager.PowerShell.dll-Help.xml
Module Name: Microsoft.Windows.ServerManager.Migration
ms.date: 01/03/2017
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.servermanager.migration/receive-smigserverdata?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Receive-SmigServerData
---

# 接收 SmigServer 数据

## 摘要
允许目标服务器接收从源服务器迁移过来的共享资源（包括文件夹、文件及相关权限和共享属性）。在目标服务器上运行 `Receive-SmigServerData` 命令的同时，必须在源服务器上也运行 `Send-SmigServerData` 命令。

## 语法

```
Receive-SmigServerData -Password <SecureString> [<CommonParameters>]
```

## 描述
**Receive-SmigServerData** cmdlet 允许目标服务器通过端口 7000 接收从源服务器迁移过来的共享资源（包括文件夹、文件及其相关权限和属性）。要发送数据，必须在源服务器上先运行 **Send-SmigServerData** cmdlet。默认情况下，**Receive-SmigServerData** cmdlet 最多会等待 5 分钟来与源服务器上的 **Send-SmigServerData** cmdlet 建立连接。您可以使用注册表键来更改这个默认的最大连接时间；有关此注册表设置的更多信息，请参阅“备注”部分。

在本次发布的 Windows Server 中，您可以在不一定位于同一子网中的服务器之间发送和接收数据。同时，您也可以使用 IP 地址来指定源服务器或目标服务器的名称。为了支持跨子网的迁移（即通过指定 IP 地址来进行迁移），必须在源服务器和目标服务器上打开端口 7001 和 7002。

文件访问权限在迁移过程中会得到保留；迁移完成后，同一组用户仍然能够访问目标服务器上的文件。由于文件是通过加密连接传输的，因此需要在源服务器和目标服务器上提供密码才能解密这些文件。目前不支持传输加密文件（EFS）和 Junction Point（一种文件链接机制）。

有关 Windows Server 迁移工具 cmdlet 的在线帮助，请参阅 [Windows PowerShell 中的服务器迁移 cmdlet](https://go.microsoft.com/fwlink/?LinkId=246313)（网址：http://go.microsoft.com/fwlink/?LinkId=246313）。

## 示例

### 示例 1：接收服务器数据
```
PS C:\> Receive-SmigServerData
```

此命令用于接收通过 `Send-SmigServerData` cmdlet 从源计算机迁移过来的数据。由于该示例命令中未提供密码，因此在输入命令后，系统会提示用户输入用于解密迁移数据的密码。密码字符会显示为星号（*）。当用户输入密码后，该密码会以 `SecureString` 的形式传递给命令。

### 示例 2：使用指定的密码接收服务器数据
```
PS C:\> Receive-SmigServerData -Password (Read-Host "Enter a Password:" -AsSecureString)
```

该命令接收从源计算机通过 `Send-SmigServerData` cmdlet 迁移过来的数据。同时，该命令还会指示迁移工具显示字符串 “Enter a Password:”，以提示用户输入用于解密迁移数据的密码。密码字符会以星号（*）的形式显示。当用户输入密码后，该密码会作为 `SecureString` 类型传递给命令进行处理。

### 示例 3：创建一个密码变量并接收服务器数据
```
PS C:\> $pass = ConvertTo-SecureString -String "password" -AsPlainText -Force
PS C:\> Receive-SmigServerData -Password $pass
```

在这个例子中，命令的第一行指示迁移工具将数据解密密码（用“password”表示）转换为一个安全的字符串，并将其存储在变量 `$pass` 中。

示例命令的第二行接收通过 `cmdlet Send-SmigServerData` 从源计算机迁移过来的数据。该命令还将第一个命令中指定的变量 `$pass` 的值设置为用于解密数据传输的密码。

## 参数

### -Password
使用此参数来指定密码（以安全字符串的形式），以便通过使用 256 位高级加密标准（AES）对数据传输进行解密。该安全字符串可以通过输入命令 `Read-Host -AsSecureString` 或 `ConvertTo-SecureString` 来获取。

您必须指定一个密码来保护您的数据，因为迁移后的数据会通过网络进行传输。如果您在命令中未添加“Password”参数，在输入命令后系统会提示您输入密码。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注
* The Windows Server Migration Tools deployment log file is located in %windir%\Logs\SmigDeploy.log. Other Windows Server Migration Tools log files are created at the following locations:


- %windir%\Logs\ServerMigration.log

- On Windows Server 2008 and later versions: %localappdata%\SvrMig\Log

- On Windows Server 2003: %userprofile%\Local Settings\Application Data\SvrMig\Log

如果无法在这些位置创建日志文件，则 ServerMigration.log 和 SmigDeploy.log 将被创建在 %temp% 目录下，其他日志文件将创建在 %windir%\System32 目录下。

所有日志文件的最大大小（以MB为单位）存储在以下注册表键中。当日志文件的大小超过注册表键中指定的值时，该日志文件将被删除。然后会从一个新的日志文件开始记录数据，这个新文件的名称和路径与之前的相同。默认的最大日志文件大小为200 MB。


- Key: HKLM\Software\Microsoft\ServerMigration

- Value: MaxLogSize (REG_DWORD)

- Data: Whole numbers between 1 and 1000 (represents log size, in MB)

`Send-SmigServerData` 和 `Receive-SmigServerData` 这两个 cmdlet 的最大连接时间存储在以下注册表键中。如果在指定的时间内无法建立连接，这两个操作将会停止。默认的最大连接时间为 300 秒（即五分钟）。


- Key: HKLM\Software\Microsoft\ServerMigration

- Value: MaxConnectionTime  (REG_DWORD)

- Data: Between 1 and 3600 (represents connection time, in seconds).
If a value larger than 3600 is specified, 3600 seconds is used as the maximum connection time.

## 相关链接

[Send-SmigServerData](./Send-SmigServerData.md)

