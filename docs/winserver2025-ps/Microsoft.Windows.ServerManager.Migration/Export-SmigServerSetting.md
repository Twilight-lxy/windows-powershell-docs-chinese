---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.ServerManager.PowerShell.dll-Help.xml
Module Name: Microsoft.Windows.ServerManager.Migration
ms.date: 01/03/2017
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.servermanager.migration/export-smigserversetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Export-SmigServerSetting
---

# Export-SmigServerSetting

## 摘要
从本地计算机导出选定的 Windows 功能和操作系统设置，并将它们存储在迁移存储库中。

## 语法

```
Export-SmigServerSetting [-FeatureId <String[]>] [-Feature <Feature[]>] [-User <String>] [-Group] [-IPConfig]
 -Path <String> -Password <SecureString> [<CommonParameters>]
```

## 描述
**Export-SmigServerSetting** cmdlet 用于将本地计算机上选定的 Windows 功能和操作系统设置导出，并将其存储在由 *Path* 参数指定的迁移存储库中。可以使用 **Import-SmigServerSetting** cmdlet 从该迁移存储库中将这些 Windows 功能和操作系统设置导入到目标计算机。

有关 Windows Server 迁移工具 cmdlet 的在线帮助，请参阅 [Windows PowerShell 中的服务器迁移 cmdlet](https://go.microsoft.com/fwlink/?LinkId=246313)（网址：http://go.microsoft.com/fwlink/?LinkId=246313）。

## 示例

### 示例 1：导出 DHCP 服务器
```
PS C:\> Export-SmigServerSetting -Feature "DHCP" -User All -Group -Path "c:\temp\store" -Verbose
```

这个示例命令用于导出动态主机配置协议（DHCP）服务器以及DHCP服务器所需的所有其他Windows Server功能。该命令还会将本地用户账户、本地组及组成员关系导出到指定路径（即*Path*参数所指定的位置c:\temp\store）。

需要创建一个密码来加密迁移存储的数据。由于这个示例命令中没有提供密码，因此在输入命令后，系统会提示用户输入用于加密迁移数据的密码。密码字符会以星号（*）的形式显示。当用户输入密码后，该密码会被作为`SecureString`类型的数据传递给相应的命令。

通过使用 `verbose` 参数，该命令还会显示有关迁移操作的详细信息。

### 示例 2：导出 IP 配置设置
```
PS C:\> Export-SmigServerSetting -IPConfig -Path "c:\temp\store" -Password (Read-Host "Create a Password:" -AsSecureString) -Verbose
```

这个示例命令会导出基本的 IP 配置设置，并将这些数据存储在由 *Path* 参数指定的迁移存储位置（即 c:\temp\store）。该命令还会指示迁移工具显示文本字符串 “Create a Password:”，以提示用户为加密迁移存储创建密码。密码字符会以星号 (*) 的形式显示。当新密码输入完成后，**Export-SmigServerSetting** 会将这个密码值作为 SecureString 类型进行存储。

通过使用 `verbose` 参数，该命令还会显示有关迁移操作的详细信息。

### 示例 3：导出 Windows Server 的功能
```
PS C:\> $c = Get-SmigServerFeature
PS C:\> Export-SmigServerSetting -Feature $c -Path "c:\temp\store" -Verbose
```

这个示例命令用于导出一组已经通过 `Get-SmigServerFeature` cmdlet 指定的 Windows 功能。在该示例中，迁移工具被指示使用变量 `$c` 来表示由 `Get-SmigServerFeature` cmdlet 指定的功能。

第一个命令使用 `Get-SmigServerFeature` cmdlet 获取指定的 Windows 功能对象，并将它们保存在 `$c` 变量中。第二个命令导出由 `$c` 变量表示的 Windows 功能，并将这些数据存储在 *Path* 参数指定的位置（即 `c:\temp\store`）。

需要创建一个密码来加密迁移存储的数据。由于此示例命令中没有提供密码，因此在输入命令后，系统会提示用户输入用于加密迁移数据的密码。密码字符会以星号（*）的形式显示。当用户输入密码后，该密码会作为`SecureString`类型的数据传递给相应的命令。

通过使用 `verbose` 参数，该命令还会显示有关迁移操作的详细信息。

### 示例 4：导出用户账户
```
PS C:\> $pass = ConvertTo-SecureString -String "password" -AsPlainText -Force
PS C:\> Export-SmigServerSetting -User All -Password $pass -Path "c:\store" -Verbose
```

在这个例子中，第一个命令指示迁移工具将存储加密密码（用“password”表示）转换为一个安全的字符串，并将其存储在变量 $pass 中。第二个命令导出所有本地用户账户，将变量 $pass 的值设置为用于加密迁移存储的密码，并将迁移数据存储在 c:\temp\store 目录中。

通过使用 `verbose` 参数，该命令还会显示有关迁移操作的详细信息。

## 参数

### -Feature
指定要从源计算机导出的 Windows 功能。并非所有 Windows 功能都可以通过迁移 cmdlet 进行迁移。您可以使用 Get-SmigServerFeature cmdlet 获取可以从本地服务器迁移的 Windows 功能列表，然后将该列表传递给 Export-SmigServerSetting cmdlet。传递方式可以是直接将结果输出到 cmdlet，也可以先将结果存储在变量中，再在命令中使用该变量来表示这些功能。

```yaml
Type: Feature[]
Parameter Sets: (All)
Aliases: F

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -FeatureId
指定要从源计算机导出的Windows功能的ID。并非所有Windows功能都支持迁移。您可以使用`Get-SmigServerFeature` cmdlet来获取可以从本地服务器迁移的Windows功能及其ID列表。多个功能ID之间请使用逗号分隔。标准PowerShell通配符也是支持的。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: ID

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Group
导出源服务器的本地组信息。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IPConfig
导出源服务器的基本IP配置设置，包括网络接口卡（NIC）的相关设置（如与连接类型相关的前缀）、IPv4配置信息、用于禁用IPv6组件的注册表键值，以及全局Windows系统的IP配置参数。只有当网络接口卡处于启用状态并且已连接到网络时，才能将其IP配置信息导出。有关更多详细信息，请参阅《IP配置迁移指南》。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Password
将迁移存储的加密密码指定为一个安全字符串。该安全字符串可以通过执行 `Read-Host -AsSecureString` 或 `ConvertTo-SecureString` 命令来获取。由于“Password”参数是必需的，因此如果在命令中未添加该参数，在输入命令后系统会提示您创建一个密码。密码的长度必须至少为 6 个字符，最多为 260 个字符。

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

### -Path
指定用于存储导出迁移数据的路径。指定的迁移数据存储位置必须为空。该路径必须是有效的本地路径或通用命名规范（UNC）路径；如果它是远程计算机上的共享资源，那么在本地计算机上必须将该共享资源表示为一个驱动器字母。路径长度不能超过246个字符。不支持通配符。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -User
指定要导出到迁移存储的用户账户类型。此参数的可接受值如下：


- Enabled

- Disabled

- All

用户密码没有被迁移。用户必须在首次登录服务器时自行创建密码。只有“用户名”和“账户已禁用”这两个属性会被迁移。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.Windows.ServerManager.Migration.MigrationResult

## 备注
* The Windows Server Migration Tools deployment log file is located in %windir%\Logs\SmigDeploy.log. Other Windows Server Migration Tools log files are created at the following locations:


- %windir%\Logs\ServerMigration.log

- On Windows Server 2008 and later versions: %localappdata%\SvrMig\Log

- On Windows Server 2003: %userprofile%\Local Settings\Application Data\SvrMig\Log

如果无法在这些位置创建日志文件，则 ServerMigration.log 和 SmigDeploy.log 会被创建在 %temp% 目录下，其他日志文件则会被创建在 %windir%\System32 目录下。

所有日志文件的最大大小（以MB为单位）存储在以下注册表键中。当日志文件的大小超过注册表键中指定的值时，该日志文件会被删除。然后系统会从一个新的日志文件开始记录数据，这个新文件的名称和路径与之前的相同。默认的最大日志文件大小为200 MB。


- Key: HKLM\Software\Microsoft\ServerMigration

- Value: MaxLogSize (REG_DWORD)

- Data: Whole numbers between 1 and 1000 (represents log size, in MB)

## 相关链接

[Import-SmigServerSetting](./Import-SmigServerSetting.md)

