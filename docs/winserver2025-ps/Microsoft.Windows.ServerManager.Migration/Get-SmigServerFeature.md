---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.ServerManager.PowerShell.dll-Help.xml
Module Name: Microsoft.Windows.ServerManager.Migration
ms.date: 01/03/2017
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.servermanager.migration/get-smigserverfeature?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-SmigServerFeature
---

# Get-SmigServerFeature

## 摘要
获取可以从本地服务器或迁移存储库中迁移的所有Windows功能的集合。

## 语法

### `empty`（默认值）
```
Get-SmigServerFeature [<CommonParameters>]
```

### TargetPreview
```
Get-SmigServerFeature -Path <String> -Password <SecureString> [<CommonParameters>]
```

## 描述
`Get-SmigServerFeature` cmdlet 可以获取所有可以从本地服务器或迁移存储库中迁移的 Windows Server 功能列表。如果在 `Path` 参数中指定了迁移存储库，该 cmdlet 仅会返回那些可以安装到本地服务器上的迁移存储库中的功能。

有关 Windows Server 迁移工具 cmdlet 的在线帮助，请参阅 [Windows PowerShell 中的服务器迁移 cmdlet](https://go.microsoft.com/fwlink/?LinkId=246313)（网址：http://go.microsoft.com/fwlink/?LinkId=246313）。

## 示例

### 示例 1：获取所有 Windows Server 功能
```
PS C:\> Get-SmigServerFeature
```

该命令会显示所有可以从本地计算机迁移到的Windows功能。

### 示例 2：在指定路径获取 Windows Server 功能
```
PS C:\> Get-SmigServerFeature -Path "c:\temp\store"
```

此命令用于检索并显示可以从由 *Path* 参数指定的迁移存储位置（位于 c:\temp\store）中迁移出来的 Windows 功能集。由于该示例命令中没有提供密码，因此在输入命令后，系统会提示用户输入密码以解密迁移存储数据。密码字符将以星号 (*) 的形式显示。当用户输入密码后，该密码会被作为 SecureString 类型传递给命令执行。

### 示例 3：获取 Windows Server 的功能并显示密码提示
```
PS C:\> $c = Get-SmigServerFeature -Path "c:\temp\store" -Password (Read-Host "Enter a Password:" -AsSecureString)
```

命令的第一行使用了 **Get-SmigServerFeature** cmdlet 来从由 *Path* 参数指定的位置处的迁移存储中检索角色或功能对象，并将它们保存到 $c 变量中。

该命令还指示迁移工具显示字符串“请输入密码：”，以提示用户输入用于解密迁移存储的密码。密码字符会以星号（*）的形式显示。当用户输入密码后，该密码值将以SecureString的形式传递给命令。

#### 示例 4：获取 Windows Server 的功能并将其导入
```
PS C:\> Get-SmigServerFeature -Path "c:\temp\store" | Import-SmigServerSetting -Path "c:\temp\store" -Verbose
```

The first part of the command, before the pipe (|) character, retrieves all role or feature objects listed by using the **Get-SmigServerFeature** cmdlet that are found in the store specified by the *Path* parameter.
The second part of the command imports those Windows features that are both listed by **Get-SmigServerFeature** and available in the migration store.

由于这个示例命令中没有提供密码，在输入命令后，系统会提示用户输入密码以解密迁移存储数据。密码字符会显示为星号（*）。当用户输入密码后，该密码会以 `SecureString` 的形式传递给命令。

通过使用 `Verbose` 参数，该命令还会显示有关迁移操作的详细信息。

### 示例 5：创建一个安全的密码变量以获取 Windows Server 功能并将其导入
```
PS C:\> $pass = ConvertTo-SecureString -String "password" -AsPlainText -
PS C:\> Get-SmigServerFeature -Path "c:\temp\store" -Password $pass | Import-SmigServerSetting -Path "c:\temp\store" -Password $pass -Verbose
```

第一个命令将表示为“password”的商店加密密码转换为一个安全的字符串，并将其存储在变量 $pass 中。

第二个命令分为两部分。第一部分使用 **Get-SmigServerFeature** cmdlet 来检索可以从由 *Path* 参数指定的迁移存储（位于 c:\temp\store）中迁移的 Windows 功能集，并提供用于解密该迁移存储的密码（存储在变量 $pass 中）。命令的第二部分将 Get cmdlet 所获取的 Windows 功能传递给 Import-SmigServerSetting cmdlet，以便在目标计算机上安装这些功能。同样，这个命令也通过变量 $pass 提供了解密迁移存储所需的密码。

通过使用 `Verbose` 参数，该命令还会显示有关迁移操作的详细信息。

## 参数

### -Password
指定用于解密迁移存储的密码（以安全字符串的形式）。该安全字符串可以通过执行 `Read-Host -AsSecureString` 或 `ConvertTo-SecureString` 命令来获取。

```yaml
Type: SecureString
Parameter Sets: TargetPreview
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定用于检索 Windows 功能的迁移存储路径。该路径必须是一个格式正确的本地路径或通用命名 convention (UNC) 路径；如果它是远程计算机上的共享资源，则需要在本地计算机上用驱动器字母表示该共享资源。路径长度不能超过 246 个字符，不支持通配符。返回的 Windows 功能列表仅包含同时存在于迁移存储中且可在本地计算机上安装的那些功能。

```yaml
Type: String
Parameter Sets: TargetPreview
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.Windows.ServerManager.Migration.Feature[]
获取所有可以从本地服务器或迁移存储库中迁移的 Windows 功能集合。如果在 *Path* 参数中指定了迁移存储库，此 cmdlet 仅返回可以安装在本地服务器上的那些位于迁移存储库中的功能。

## 备注
* The Windows Server Migration Tools deployment log file is located in %windir%\Logs\SmigDeploy.log. Other Windows Server Migration Tools log files are created at the following locations:


- %windir%\Logs\ServerMigration.log

- On Windows Server 2008 and later versions: %localappdata%\SvrMig\Log

- On Windows Server 2003: %userprofile%\Local Settings\Application Data\SvrMig\Log

如果无法在这些位置创建日志文件，那么 ServerMigration.log 和 SmigDeploy.log 将会被创建在 %temp% 目录下，其他日志文件则会被创建在 %windir%\System32 目录下。

所有日志文件的最大大小（以MB为单位）存储在以下注册表键中。当日志文件的大小超过该注册表键中指定的值时，该日志文件会被删除。随后会使用相同的文件名和路径创建一个新的日志文件，并重新开始记录日志。默认的最大日志文件大小为200 MB。


- Key: HKLM\Software\Microsoft\ServerMigration

- Value: MaxLogSize (REG_DWORD)

- Data: Whole numbers between 1 and 1000 (represents log size, in MB)

## 相关链接

