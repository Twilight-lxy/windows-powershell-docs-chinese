---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.ServerManager.PowerShell.dll-Help.xml
Module Name: Microsoft.Windows.ServerManager.Migration
ms.date: 01/03/2017
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.servermanager.migration/import-smigserversetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-SmigServerSetting
---

# 导入 SmigServerSetting

## 摘要
从迁移存储中导入选定的Windows功能及操作系统设置，并将其应用到本地计算机上。

## 语法

```
Import-SmigServerSetting [-Feature <Feature[]>] [-FeatureId <String[]>] [-Group]
 [-SourcePhysicalAddress <String[]>] [-TargetPhysicalAddress <String[]>] [-Force] -Path <String>
 [-User <String>] [-IPConfig <String>] -Password <SecureString> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Import-SmigServerSetting** 这个 cmdlet 会从由 *Path* 参数指定的迁移存储库中导入选定的 Windows 功能和操作系统设置，并将其应用到本地计算机上。在运行此 cmdlet 之前，您必须先使用 **Export-SmigServerSetting** cmdlet 将 Windows 功能及设置从源服务器导出到该迁移存储库中。设置的应用顺序是无法保证的。如果某些设置需要按特定顺序进行迁移，则需要多次运行 **Import-SmigServerSetting** cmdlet 以按照所需顺序应用这些设置。此外，如果您要迁移的 Windows 功能尚未安装，此 cmdlet 还可用于安装这些功能及其依赖项。某些 Windows 功能可能需要重新启动目标计算机才能完成安装过程。在重启计算机后，您需要再次运行该 cmdlet 并使用 *Force* 参数来完成导入操作。

有关 Windows Server 迁移工具 cmdlet 的在线帮助，请访问 [http://go.microsoft.com/fwlink/?LinkId=246313](https://go.microsoft.com/fwlink/?LinkId=246313)。

## 示例

### 示例 1：导入 DHCP 服务器
```
PS C:\> Import-SmigServerSetting -Feature "DHCP" -User All -Group -Path "c:\temp\store" -Verbose
```

这个示例命令用于导入动态主机配置协议（DHCP）服务器以及该技术所需的所有其他Windows功能。同时，该命令还将本地用户账户、本地组及其组成员关系导入到由*Path*参数指定的路径c:\temp\store中。

需要输入密码来解密迁移存储的数据。由于这个示例命令中没有提供密码，因此在用户输入命令后，系统会提示用户输入用于加密迁移数据的密码。密码字符会以星号（*）的形式显示。当密码输入完成后，该密码会被作为`SecureString`类型的数据传递给相应的命令。

通过使用 `Verbose` 参数，该命令还会显示有关迁移操作的详细信息。

### 示例 2：导入 IP 配置
```
PS C:\> Import-SmigServerSetting -IPConfig All -SourcePhysicalAddress "00-13-D3-F7-A1-3A","00-13-D3-F7-A1-4A" -TargetPhysicalAddress "11-13-D3-F7-A1-3A","11-13-D3-F7-A1-4A" -Path "c:\temp\store" -Password (Read-Host "Enter a Password:" -AsSecureString)-Verbose
```

此命令从位于 c:\temp\store 的迁移存储中导入 IP 配置，并将其应用到本地服务器上。物理地址为 00-13-D3-F7-A1-3A 的网络接口卡（NIC）上的 IP 配置会被迁移到物理地址为 11-13-D3-F7-A1-3A 的 NIC 上；同样，物理地址为 00-13-D3-F7-A1-4A 的 NIC 上的 IP 配置也会被迁移到物理地址为 11-13-D3-F7-A1-4A 的 NIC 上。此外，该命令还指示迁移工具导入 Windows 的 IP 配置设置，例如 DNS 后缀搜索列表设置以及禁用 IPv6 的注册表键值。

该命令还指示迁移工具显示字符串“请输入密码：”，以提示用户输入用于解密迁移存储的密码。密码字符会显示为星号（*）。当用户输入密码后，该密码值会以SecureString的形式传递给命令。

通过使用 `Verbose` 参数，该命令还会显示有关迁移操作的详细信息。

### 示例 3：获取 Windows Server 的功能并将其导入
```
PS C:\> $c = Get-SmigServerFeature -Path "c:\temp\store"
PS C:\> Import-SmigServerSetting -Feature $c -Path "c:\temp\store" -Verbose
```

该命令导入了一组Windows功能，这些功能是通过使用Get-SmigServerFeature cmdlet预先获取的。

命令的第一行使用 **Get-SmigServerFeature** cmdlet 获取指定的角色或功能对象，并将它们保存在 `$c` 变量中。命令的第二行从由 *Path* 参数（即 `c:\temp\store`）指定的迁移存储库中导入 `$c` 变量所表示的 Windows 功能。

需要输入密码来解密迁移存储的数据。由于这个示例命令中没有提供密码，因此在用户输入命令后，系统会提示用户输入用于加密迁移数据的密码。密码字符会以星号（*）的形式显示。当密码输入完成后，该密码会被作为`SecureString`类型的数据传递给相应的命令。

通过使用 `Verbose` 参数，该命令还会显示有关迁移操作的详细信息。

### 示例 4：获取 Windows Server 的功能并将它们导入
```
PS C:\> Get-SmigServerFeature -Path "c:\temp\store" | Import-SmigServerSetting -Path "c:\temp\store" -Verbose
```

这条命令将之前通过使用 `Get-SmigServerFeature` cmdlet 获取到的一组特征数据，传递给 `Import-SmigServerSetting` cmdlet。

The first part of the command, before the pipe (|) character, retrieves all role or feature objects listed by using the **Get-SmigServerFeature** cmdlet that are found in the store specified by the *Path* parameter.
The second part of the command imports those Windows features that are both listed by **Get-SmigServerFeature** and available in the migration store.

需要输入密码来解密迁移存储的数据。由于这个示例命令中没有提供密码，因此在用户输入命令后，系统会提示用户输入用于加密迁移数据的密码。密码字符会以星号（*）的形式显示。当密码输入完成后，该密码会被作为`SecureString`类型的数据传递给相应的命令。

通过使用 `Verbose` 参数，该命令还会显示有关迁移操作的详细信息。

### 示例 5：创建一个密码变量，并使用它来导入用户账户
```
PS C:\> $pass = ConvertTo-SecureString -String "password" -AsPlainText -Force
PS C:\> Import-SmigServerSetting -User All -Password $pass -Path "c:\store" -Verbose
```

在这个示例中，第一个命令将用于存储加密数据的密码（用“password”表示）转换为一个安全的字符串，并将其存储在变量 `$pass` 中。第二个命令导入所有本地用户账户，并使用变量 `$pass` 的值作为密码来解密迁移数据存储中的内容。

通过使用 `Verbose` 参数，该命令还会显示有关迁移操作的详细信息。

## 参数

### -Feature
指定您想要从迁移存储库中导入的 Windows 特性对象。并非所有的 Windows 特性都可以通过迁移 cmdlet 进行迁移。您可以使用 Get-SmigServerFeature cmdlet 来获取可以从迁移存储库迁移到目标服务器的 Windows 特性列表，然后将该列表传递给 **Import-SmigServerSetting** cmdlet——可以通过将结果管道传输给该 cmdlet 来实现，或者先将结果存储在变量中，再在命令中使用该变量来表示这些结果。

此cmdlet还会安装Windows功能及其依赖项（如果你要迁移的功能尚未被安装的话）。某些Windows功能可能需要重新启动目标计算机才能完成安装。在重启计算机后，你必须再次运行该cmdlet，并使用*Force*参数来完成导入操作。

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
指定您希望从迁移存储中导入的 Windows 功能的 ID。并非所有 Windows 功能都支持迁移。您可以使用 **Get-SmigServerFeature** cmdlet 来获取 Windows 功能及其功能 ID 的列表，这些功能可以从迁移存储迁移到目标服务器。多个功能 ID 之间使用逗号分隔。标准 PowerShell 匹配通配符也是支持的。

此cmdlet还会安装Windows功能及其依赖项（如果你要迁移的功能尚未被安装的话）。某些Windows功能可能需要重新启动目标计算机才能完成安装。在重启计算机后，你必须再次运行该cmdlet，并使用*Force*参数来完成导入操作。

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

### -Force
指定导入的设置会覆盖目标计算机上现有的Windows功能设置。如果不使用此参数，则默认情况下目标计算机上的现有Windows功能设置将保持不变。

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

### -Group
从迁移存储中导入本地组及其成员信息。如果目标服务器上已经存在某个组，那么该组不会被覆盖。源服务器上的组成员信息会被添加到目标服务器上的现有组中，同时目标服务器上的原有组成员信息也会被保留下来。

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
导入源服务器的基本IP配置设置。该参数可接受以下值：


- NIC: network interface card (NIC) IP configuration settings such as connection-specific suffix, IPv4 settings and Disable IPv6 Component registry key.
IP configuration can only be imported for a NIC if it is enabled and connected to the network.
You must restart your computer for disabling IPv6 components to take effect.

- Global: Windows IP configuration settings for the local computer.

- All: both NIC and Global settings.

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

### -Password
指定用于解密迁移存储的密码（以安全字符串的形式）。该安全字符串可以通过执行 `Read-Host -AsSecureString` 或 `ConvertTo-SecureString` 命令来获取。由于 `-Password` 参数是必需的，因此如果在命令中未添加该参数，在输入命令后系统会提示您输入密码。

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
指定迁移存储的路径，您可以从该路径导入 Windows 功能和操作系统设置。该路径必须是一个格式正确的本地路径或通用命名规范（UNC）路径；如果它是远程计算机上的共享资源，则必须在本地计算机上用驱动器字母来表示该共享资源。路径长度不能超过 246 个字符。不支持通配符。由于 *Path* 参数是必需的，如果您在命令中未添加该参数，在输入命令后系统会提示您指定路径。

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

### -SourcePhysicalAddress
请用双引号指定用于导入IP设置的源网络接口卡（NIC）的物理地址。如果要指定多个源物理地址，请使用逗号分隔每个地址。源物理地址的数量必须与*TargetPhysicalAddress*参数中指定的目标物理地址数量相同。不支持通配符字符。在迁移NIC或所有IP配置时，此参数是必需的。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetPhysicalAddress
请用双引号指定目标网络接口卡（NIC）的物理地址，您希望将IP设置应用到这些地址上。如果您指定了多个目标物理地址，请使用逗号分隔每个地址。目标物理地址的数量必须与*SourcePhysicalAddress*参数中指定的源物理地址数量相同。不支持通配符字符。在迁移NIC或所有IP配置时，此参数是必需的。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -User
请指定要从迁移存储中导入的本地用户账户的类型。此参数的可接受值如下：


- Enabled: import only enabled local users

- Disabled: import only disabled local users

- All: import both enabled and disabled local users

用户密码不会被迁移。用户必须在第一次登录服务器时自行创建密码。只有“用户名”和“账户已禁用”这两个属性会被迁移。

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

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.Windows.ServerManager.Migration.MigrationResult []

## 备注
* The Windows Server Migration Tools deployment log file is located in %windir%\Logs\SmigDeploy.log. Other Windows Server Migration Tools log files are created at the following locations:


- %windir%\Logs\ServerMigration.log

- On Windows Server 2008 and later versions: %localappdata%\SvrMig\Log

- On Windows Server 2003: %userprofile%\Local Settings\Application Data\SvrMig\Log

如果无法在这些位置创建日志文件，则 ServerMigration.log 和 SmigDeploy.log 将会被创建在 %temp% 目录下，其他日志文件则会被创建在 %windir%\System32 目录下。

所有日志文件的最大大小（以MB为单位）存储在以下注册表键中。当日志文件的大小超过注册表键中指定的值时，该日志文件将被删除。随后，日志记录会重新开始，并使用相同的文件名和路径生成一个新的日志文件。默认的最大日志文件大小为200 MB。


- Key: HKLM\Software\Microsoft\ServerMigration

- Value: MaxLogSize (REG_DWORD)

- Data: Whole numbers between 1 and 1000 (represents log size, in MB)

## 相关链接

[Export-SmigServerSetting](./Export-SmigServerSetting.md)

