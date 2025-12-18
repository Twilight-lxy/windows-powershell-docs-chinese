---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/enable-sbecautologger?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-SbecAutologger
---

# 启用 SbecAutologger

## 摘要
在AutoLogger设置中，启用将事件转发到“Setup和Boot事件收集器”的功能。

## 语法

### 离线模式
```
Enable-SbecAutologger -Path <String[]> [-Logger <String[]>] [-PermLogger <String[]>] [-NoDefaultLoggers]
 [-ForceLogger] [-DismLogPath <String>] [<CommonParameters>]
```

### 在线
```
Enable-SbecAutologger -ComputerName <String[]> [-Credential <PSCredential>] [-Logger <String[]>]
 [-PermLogger <String[]>] [-NoDefaultLoggers] [-ForceLogger] [<CommonParameters>]
```

### 在线Session
```
Enable-SbecAutologger -Session <PSSession[]> [-Logger <String[]>] [-PermLogger <String[]>] [-NoDefaultLoggers]
 [-ForceLogger] [<CommonParameters>]
```

### 本地（Local）
```
Enable-SbecAutologger [-Local] [-SystemHive <String>] [-ControlSet <String>] [-Logger <String[]>]
 [-PermLogger <String[]>] [-NoDefaultLoggers] [-ForceLogger] [<CommonParameters>]
```

## 描述
`Enable-SbecAutologger` cmdlet 可以在注册表的 AutoLogger 设置中启用将事件转发到 Setup 和 Boot 事件收集器的功能。此操作不会立即影响当前正在运行的日志会话；只有在操作系统重启并且 AutoLogger 服务重新启动日志会话后，该设置才会生效。

这些更改可以应用到本地计算机、远程计算机，或者离线磁盘镜像上。

要在本地计算机上操作，请指定“Local”参数。只有在运行收集器（Collector）服务的计算机将数据发送到另一台计算机上的收集器时，才需要启用数据转发功能；否则，内核模块将无法连接到该收集器。不过，您可以将PowerShell的BootEventCollector模块复制到其他计算机上，并在那里使用它进行本地配置。

要远程操作一台计算机，请指定 *ComputerName* 或 *Session* 参数。Windows PowerShell 的远程功能用于执行这些远程操作。

要操作离线（WIM或VHD）镜像，请使用*Path*参数。

此操作会配置事件日志会话“NT Kernel Logger”（如果该会话不存在，则会创建它），以及已存在的“EventLog-System”和“SetupPlatform”，以便将这些事件发送到“Boot Event Collector”。您可以通过指定“Logger”或“PermLogger”参数来配置其他日志会话。

默认情况下，对于 NT 内核日志记录器和 EventLog-System 会话来说，或者在使用 *Logger* 参数时，事件日志会话的配置方式是：一旦计算机完成启动序列并且其上的日志记录子系统完全启动并开始正常运行，从这些会话向收集器（Collector）转发事件的机制就会自动被禁用。如果你希望某个会话能够持续不断地转发事件（就像 SetupPlatform 会话默认所做的那样），则需要使用 *PermLogger* 参数。

你只能为处于实时模式（而非写入文件模式的）会话启用转发功能；因此，默认情况下，基于文件的会话将保持不变。你可以使用 `ForceLogger` 参数将这些会话切换到实时模式，并启用转发功能。

此命令还会配置“Debug Print”过滤器注册表设置，以确保至少能够传递系统崩溃时的错误检查（Bugcheck）信息。

你必须同时启用自动记录器（AutoLogger）和BCD设置，才能将事件转发到启动事件收集器（Boot Event Collector）。

## 示例

### 示例 1：在计算机上启用 AutoLogger
```
PS C:\> Enable-SbecAutologger -ComputerName "Server01"
```

此命令在名为Server01的计算机上启用AutoLogger设置。

### 示例 2：为网络设置图像启用 AutoLogger 功能
```
PS C:\> Enable-SbecAutologger -Path "boot.wim","install.wim" -ForceLogger
```

此命令配置了用于基于网络的设置的两个图像中的AutoLogger设置，并强制将SetupPlatform会话的存储位置从文件目标切换到事件收集器目标。

### 示例 3：在 VHD 镜像中启用 AutoLogger
```
PS C:\> Enable-SbecAutologger -Path "NanoServer.vhd" -Logger "Microsoft-Windows-Setup" -ForceLogger
```

此命令配置了VHD镜像中的AutoLogger，并将安装后的日志会话（如Windows Nano Server中所使用的）切换到Boot Event Collector目标。

## 参数

### -ComputerName
指定您希望在其上执行操作的计算机的名称。您可以分别为每台计算机指定一个完全限定的域名（FQDN）、NetBIOS 名称或 IP 地址。有关更多信息，请参阅 TechNet 上的 [Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

```yaml
Type: String[]
Parameter Sets: Online
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControlSet
指定用于注册表路径的控制集键。

```yaml
Type: String
Parameter Sets: Local
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential
Parameter Sets: Online
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DismLogPath
指定用于部署映像服务与管理（Deployment Image Servicing and Management，简称DISM）日志的文件路径，在挂载映像时使用该日志。

```yaml
Type: String
Parameter Sets: Offline
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ForceLogger
在为基于文件的AutoLogger会话启用事件转发功能之前，系统会强制将这些会话切换到实时模式。如果没有这个开关，这些会话的状态将保持不变。

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

### -Local
表示在本地计算机上执行此操作。该模式允许控制设置应用的注册表路径。

```yaml
Type: SwitchParameter
Parameter Sets: Local
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Logger
指定要启用转发功能的 AutoLogger 会话。这些会话的转发功能在操作系统启动后会被自动禁用。如果在 *Logger* 或 *PermLogger* 中显式指定了某个会话，其默认设置将被覆盖。

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

### -NoDefaultLoggers
表示此操作不会自动添加默认的日志记录器会话集。

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

### -Path
指定一个包含离线 Windows 映像文件（WIM 或 VHD）完整路径的数组，这些设置将应用于这些文件。如果一个 WIM 文件包含多个映像，那么所有这些映像都会被修改。

```yaml
Type: String[]
Parameter Sets: Offline
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PermLogger
指定要启用数据转发的 AutoLogger 会话。这些会话的数据转发功能在操作系统启动后仍会保持启用状态。

在 *Logger* 或 *PermLogger* 中显式指定会话会覆盖其默认设置。

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

### -Session
指定连接到远程目标计算机的 **PSSession** 对象。可以输入一个会话对象（例如 `Get-PSSession` 或 `New-PSSession` 的输出结果），或者这些对象的数组。

```yaml
Type: PSSession[]
Parameter Sets: OnlineSession
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SystemHive
指定注册表系统中配置文件（即“hive”文件）的完整路径。

```yaml
Type: String
Parameter Sets: Local
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无

## 备注

## 相关链接

[ Disable-SbecAutologger](./Disable-SbecAutologger.md)

[ Disable-SbecBcd](./Disable-SbecBcd.md)

[Enable-SbecBcd](./Enable-SbecBcd.md)

[Enable-SbecBootImage](./Enable-SbecBootImage.md)

