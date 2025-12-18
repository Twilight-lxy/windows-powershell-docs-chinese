---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/disable-sbecautologger?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-SbecAutologger
---

# 禁用 SbecAutologger

## 摘要
在 AutoLogger 的设置中，禁用将事件转发到 Setup 和 Boot 事件收集器的功能。

## 语法

### 离线模式
```
Disable-SbecAutologger -Path <String[]> [-Logger <String[]>] [-NoDefaultLoggers] [-DismLogPath <String>]
 [<CommonParameters>]
```

### 在线
```
Disable-SbecAutologger -ComputerName <String[]> [-Credential <PSCredential>] [-Logger <String[]>]
 [-NoDefaultLoggers] [<CommonParameters>]
```

### 在线Session
```
Disable-SbecAutologger -Session <PSSession[]> [-Logger <String[]>] [-NoDefaultLoggers] [<CommonParameters>]
```

### 本地（Local）
```
Disable-SbecAutologger [-Local] [-SystemHive <String>] [-ControlSet <String>] [-Logger <String[]>]
 [-NoDefaultLoggers] [<CommonParameters>]
```

## 描述
`Disable-SbecAutologger` cmdlet 会禁用将事件转发到注册表中 AutoLogger 设置中的“Setup 和 Boot 事件收集器”的功能。这一操作不会立即影响当前正在运行的日志记录会话，但会在操作系统重启后以及 AutoLogger 服务重新启动日志记录会话时生效。

这些更改可以应用到本地计算机、远程计算机，或者离线的磁盘镜像上。

要在本地计算机上执行操作，请指定“Local”参数。只有在运行Collector服务的计算机将数据发送到另一台计算机上的Collector时，启用该功能才有意义；否则，内核中的模块将无法连接到Collector。不过，您可以将PowerShell BootEventCollector模块复制到其他计算机上，并在那里使用它进行本地配置。

要远程操作一台计算机，请指定 *ComputerName* 或 *Session* 参数。Windows PowerShell 的远程功能用于执行这些远程操作。

要操作离线（WIM或VHD）镜像，请使用*Path*参数。

如果您使用 `Enable-SbecAutologger` cmdlet 将某些日志会话从基于文件的模式转换为实时模式，那么这个命令会将之前的转换操作撤销（即恢复到基于文件的模式）。

如果 `Enable-SbecAutologger` 创建了 NT 内核日志记录会话，那么这个会话并不会被 `Disable-SbecAutologger` 删除。只是会停止将该会话中的事件转发到收集器而已。

如果通过 `Enable-SbecAutologger` 修改了“调试打印”（Debug Print）过滤设置，那么通过 `Disable-SbecAutologger` 无法撤销这一更改。

## 示例

### 示例 1：禁用自动日志记录功能
```
PS C:\> Disable-SbecAutologger -ComputerName Server01
```

此命令将禁用名为Server01的计算机上的AutoLogger设置。

## 参数

### -ComputerName
指定您想要在哪些计算机上执行该操作的名称。对于每台计算机，您可以指定一个完全限定域名（FQDN）、NetBIOS名称或IP地址。有关更多信息，请参阅TechNet上的[Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

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
指定用于注册表路径的控制集键。此参数仅在与 *Local* 参数一起使用时才有效。

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
指定用于安装镜像时存储部署映像服务与管理（DISM）日志文件的路径。

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

### -Local
表示在本地计算机上执行此操作。

这种模式允许用户控制设置应用的位置（即注册表的路径）。

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
指定一个需要禁用的 AutoLogger 会话数组。如果使用星号（*），则将禁用注册表中定义的所有会话的 EVENTNET 转发功能。

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
表示此操作不会自动将默认的日志记录器会话集（EventLog-System、NT Kernel Logger 和 SetupPlatform）添加到由 *Logger* 参数指定的会话中。

如果 `Logger` 的值为 `*`，则此参数无效。

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
指定要应用设置的离线 Windows 镜像文件（WIM 或 VHD）的完整路径列表。如果一个 WIM 文件包含多个镜像，那么所有这些镜像都会被修改。

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

### -SystemHive
指定注册表路径对应的系统hive（配置文件）的完整路径。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要处理的内容）。

## 输出

### 没有（需要处理的内容）。

## 备注

## 相关链接

[Disable-SbecBcd](./ Disable-SbecBcd.md)

[Enable-SbecAutologger](./Enable-SbecAutologger.md)

[Enable-SbecBcd](./Enable-SbecBcd.md)

[Enable-SbecBootImage](./Enable-SbecBootImage.md)

