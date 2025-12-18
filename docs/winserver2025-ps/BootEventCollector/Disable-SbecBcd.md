---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BootEventCollector-help.xml
Module Name: BootEventCollector
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/booteventcollector/disable-sbecbcd?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-SbecBcd
---

# 禁用 SbecBcd

## 摘要
在BCD设置中禁用事件转发模式。

## 语法

### 离线模式
```
Disable-SbecBcd -Path <String[]> [-Id <String>] [-DismLogPath <String>] [<CommonParameters>]
```

### 在线
```
Disable-SbecBcd -ComputerName <String[]> [-Credential <PSCredential>] [-Id <String>] [<CommonParameters>]
```

### 在线Session
```
Disable-SbecBcd -Session <PSSession[]> [-Id <String>] [<CommonParameters>]
```

### 本地
```
Disable-SbecBcd [-Local] [-BcdStore <String>] [-Id <String>] [<CommonParameters>]
```

## 描述
`Disable-SbecBcd` cmdlet 用于禁用启动配置数据（Boot Configuration Data, BCD）中的 `/event*` 标志。此操作对当前的连接没有影响；必须重新启动计算机才能使设置生效。

你可以将这些更改应用到本地计算机、远程计算机，或者离线磁盘镜像上。

要在本地计算机上操作，请指定“Local”参数。只有在将数据发送到另一台计算机上的收集器（Collector）时，才有必要在运行收集器服务的计算机上启用数据转发功能；否则，内核模块无法与收集器建立连接。不过，您可以将 PowerShell 的 BootEventCollector 模块复制到其他计算机上，并在那里使用它进行本地配置。

要操作远程计算机，请指定 *ComputerName* 或 *Session* 参数。Windows PowerShell 的远程功能用于执行这些远程操作。

要操作离线（WIM或VHD）镜像，请使用*Path*参数。WIM镜像通常不包含BCD文件，而且也很少需要替换这些文件。相反，Windows安装程序在将WIM镜像解压到硬盘时才会生成BCD设置。

## 示例

### 示例 1：禁用 BCD（Binary-Coded Decimal）
```
PS C:\> Disable-SbecBcd -Session $MyPSSession
```

此命令会禁用远程会话中的BCD（Binary-Coded Decimal）设置。

## 参数

### -BcdStore
指定 BCD 存储的完整路径。

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

### -ComputerName
指定您想要在其上执行操作的计算机的名称。您可以分别为每台计算机指定一个完全限定的域名（FQDN）、NetBIOS名称或IP地址。有关更多信息，请参阅TechNet上的[Invoke-CimMethod](https://go.microsoft.com/fwlink/?LinkId=808801)。

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
指定用于安装镜像时存储部署图像服务与管理（DISM）日志文件的路径。

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
指定要禁用的条目的ID，无需使用大括号。

BCD（Binary-Coded Decimal）设置中可能包含多个启动镜像的条目（当计算机安装了多个操作系统版本时）。如果需要修改当前正在运行的操作系统之外的其他操作系统的设置（或者在离线镜像中的默认操作系统设置），可以使用这个参数来选择相应的条目。

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

### -Local
表示此操作是在本地计算机上执行的。该模式还提供了对设置应用位置的额外控制（即对BCD存储器的控制）。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 没有（需要说明的内容）。

## 输出

### 没有（需要说明的内容）。

## 备注

## 相关链接

[Disable-SbecAutologger](./ Disable-SbecAutologger.md)

[Enable-SbecAutologger](./Enable-SbecAutologger.md)

[Enable-SbecBcd](./Enable-SbecBcd.md)

[Enable-SbecBootImage](./Enable-SbecBootImage.md)

[Enable-SbecWdsBcd](./Enable-SbecWdsBcd.md)

