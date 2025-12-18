---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/enable-sbecbcd?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-SbecBcd
---

# Enable-SbecBcd

## 摘要
在BCD设置中启用并配置事件转发模式。

## 语法

### 离线
```
Enable-SbecBcd -Path <String[]> -CollectorIp <String> -CollectorPort <String> -Key <String> [-Id <String>]
 [-BusParameters <String>] [-DismLogPath <String>] [<CommonParameters>]
```

### 在线
```
Enable-SbecBcd -ComputerName <String[]> [-Credential <PSCredential>] -CollectorIp <String>
 -CollectorPort <String> -Key <String> [-Id <String>] [-BusParameters <String>] [<CommonParameters>]
```

### 在线Session
```
Enable-SbecBcd -Session <PSSession[]> -CollectorIp <String> -CollectorPort <String> -Key <String>
 [-Id <String>] [-BusParameters <String>] [<CommonParameters>]
```

### 本地（Local）
```
Enable-SbecBcd [-Local] [-BcdStore <String>] [-CreateEventSettings] -CollectorIp <String>
 -CollectorPort <String> -Key <String> [-Id <String>] [-BusParameters <String>] [<CommonParameters>]
```

## 描述
`Enable-SbecBcd` cmdlet 用于配置 BCD（Boot Configuration Data）中的安装和启动事件收集器设置。该命令会启用 `/event` 标志，并在 BCD 的 `/eventsettings` 中设置收集器的主机 IP 地址、端口以及加密密钥。

此操作对当前的连接没有立即影响；它会在操作系统重启后才会生效。

这些更改可以应用到本地计算机、远程计算机或离线磁盘镜像上。

要在本地计算机上进行操作，请指定“Local”参数。只有当运行收集器服务的计算机将数据发送到另一台计算机上的收集器时，才有必要在该计算机上启用数据转发功能；否则，内核中的模块将无法连接到收集器。不过，您可以将PowerShell BootEventCollector模块复制到其他计算机上，并在那里使用它进行本地配置。

要远程操作一台计算机，请指定 *ComputerName* 或 *Session* 参数。Windows PowerShell 的远程功能用于执行这些远程操作。

要操作离线（WIM或VHD）镜像，请使用*Path*参数。WIM镜像通常不包含BCD文件，也几乎没有必要将它们放入镜像中。相反，Windows安装程序在从WIM镜像提取内容到硬盘驱动器时才会创建BCD设置。

你必须同时启用自动日志记录（AutoLogger）和BCD设置，才能将事件转发到启动事件收集器（Boot Event Collector）。

## 示例

### 示例 1：为远程会话配置 BCD 设置
```
PS C:\> Enable-SbecBcd -Session $MyPSSession -CollectorIp 192.168.1.1 -CollectorPort "50000" -Key "a.b.c.d"
```

此命令用于配置远程会话的BCD（Binary-Coded Decimal）设置。

## 参数

### -BcdStore
指定 BCD 存储文件的完整路径。

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

### -BusParameters
指定用于选择目标计算机上用于通信的网络适配器（NIC）的总线参数。此值会覆盖系统默认选择的第一个受支持的适配器。

这个值适用于所有使用该镜像的计算机；只有当这些计算机的硬件具有足够的同质性时，才能使用该值。

要找到机器上某个特定网络接口卡（NIC）的总线参数值，请打开“设备管理器”，在“网络适配器”中选择所需的网络适配器。右键点击该适配器，选择“属性”，然后选择“详细信息”选项卡，再选择“位置信息”。系统会显示一段如下形式的字符串：PCI 总线 X，设备 Y，功能 Z。本例中需要指定的总线参数就是 “X,Y,Z”。

```yaml
Type: String
Parameter Sets: (All)
Aliases: BusParams

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CollectorIp
指定托管“启动事件收集器”（Boot Event Collector）的主机的IPv4地址。

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

### -CollectorPort
指定端口号（该端口号通常同时适用于目标系统和数据收集器）。

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

### -ComputerName
指定您希望在其上执行操作的计算机名称。您可以分别为每台计算机指定一个完全限定域名（FQDN）、NetBIOS名称或IP地址。有关更多信息，请参阅TechNet上的[Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

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

### -CreateEventSettings
这表示该操作会明确创建 `{eventsettings}` 键，这是 WDS 生成的 BCD 文件所必需的。

```yaml
Type: SwitchParameter
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
指定用于部署映像服务和管理（DISM）日志的文件路径，在挂载映像时使用该日志。

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

### -Id
指定要修改的条目的ID，无需使用大括号。BCD设置中可能包含多个启动镜像的条目（当计算机安装了多个操作系统版本时）。如果需要修改当前正在运行的操作系统以外的其他操作系统的设置（或离线镜像中的默认操作系统设置），可以使用此参数来选择相应的条目。

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

### -Key
指定用于通信的加密密钥。该值必须与为此目标收集器配置中指定的密钥相匹配。

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

### -Local
表示此操作是在本地计算机上执行的。这种模式还允许对BCD存储进行额外的控制，从而可以指定设置应用的位置。

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

### -Path
指定要应用这些设置的离线Windows镜像文件（WIM或VHD）的完整路径列表。如果一个WIM文件包含多个镜像，那么所有这些镜像都会被修改。

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

### -Session
指定连接到远程目标计算机的 **PSSession** 对象。可以输入一个会话对象（例如 `Get-PSSession` 或 `New-PSSession` 命令的输出结果），或者这些对象的数组。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 名称

## 输出

### 名称

## 备注

## 相关链接

[Disable-SbecAutologger](./Disable-SbecAutologger.md)

[Disable-SbecBcd](./Disable-SbecBcd.md)

[Enable-SbecAutologger](./Enable-SbecAutologger.md)

[Enable-SbecBootImage](./Enable-SbecBootImage.md)

[Enable-SbecWdsBcd](./Enable-SbecWdsBcd.md)

