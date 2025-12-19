---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: iSCSITargetPortal.cdxml-help.xml
Module Name: iSCSI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsi/update-iscsitargetportal?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Update-IscsiTargetPortal
---
# 更新 IScsiTargetPortal

## 摘要
更新有关指定的 iSCSI 目标门户的信息。

## 语法

### 按目标门户地址（默认）

```
Update-IscsiTargetPortal [-TargetPortalAddress] <String[]> [-InitiatorInstanceName <String>]
 [-InitiatorPortalAddress <String>] [-TargetPortalPortNumber <UInt16>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

### InputObject（cdxml）

```
Update-IscsiTargetPortal -InputObject <CimInstance[]> [-InitiatorInstanceName <String>]
 [-InitiatorPortalAddress <String>] [-TargetPortalPortNumber <UInt16>] [-CimSession <CimSession[]>]
 [-ThrottleLimit <Int32>] [-AsJob] [-PassThru] [<CommonParameters>]
```

## 描述

`Update-IscsiTargetPortal` cmdlet 用于刷新关于 iSCSI 目标端口的缓存信息。

## 示例

### 示例 1：更新关于 iSCSI 目标端点的信息

这个命令用于更新关于指定的 iSCSI 目标端口的信息。第一个命令使用 **Get-IscsiTargetPortal** cmdlet 来显示所有可用的目标端口信息。

```powershell
Get-IscsiTargetPortal
```

```Output
InitiatorInstanceName      :
InitiatorNodeAddress       :
InitiatorPortalAddress     :
InititorIPAdressListNumber : 4294967295
IsDataDigest               : False
IsHeaderDigest             : False
TargetPortalAddress        : testiSCSI-deepcore
TargetPortalPortNumber     : 3260
```

```powershell
Get-IscsiTargetPortal | Update-IscsiTargetPortal
```
第二个命令将相同的目标门户传递给当前的cmdlet以对其进行更新。

## 参数

### -AsJob

将此cmdlet作为后台作业运行。使用该参数来执行需要较长时间才能完成的命令。

该 cmdlet 会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用 `*-Job` 系列 cmdlets；要获取作业结果，请使用 [Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -CimSession

在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InitiatorInstanceName

指定 iSCSI 启动器服务用于向目标门户发送 **SendTargets** 请求的启动器实例的名称。如果未指定实例名称，则 iSCSI 启动器服务会自行选择相应的启动器实例。

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

### -InitiatorPortalAddress

指定与门户关联的 IP 地址或 DNS 名称。

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

### -InputObject

指定该 cmdlet 的输入数据。您可以使用此参数，也可以将输入数据通过管道（pipe）传递给该 cmdlet。

```yaml
Type: CimInstance[]
Parameter Sets: InputObject (cdxml)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -PassThru

返回一个表示您正在操作的该项的对象。默认情况下，此 cmdlet 不会生成任何输出。

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

### -TargetPortalAddress

指定目标门户的 IP 地址或 DNS 名称。

```yaml
Type: String[]
Parameter Sets: ByTargetPortalAddress
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetPortalPortNumber

指定目标门户的TCP/IP端口号。默认情况下，端口号为`3260`。

```yaml
Type: UInt16
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit

该参数用于指定可以同时运行的命令行脚本（cmdlet）的最大操作数量。如果省略此参数或输入值`0`，则Windows PowerShell®会根据计算机上正在运行的CIM命令行脚本的数量来计算该cmdlet的最佳并发限制。此并发限制仅适用于当前正在执行的命令行脚本，而不影响整个会话或计算机本身的性能。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters

此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#MSFT_IscsiTargetPortal

`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名。

## 输出

### 无

## 备注

## 相关链接

[TechNet上的iSCSI相关内容](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee338476(v=ws.10))

[TechNet上的存储相关内容](https://go.microsoft.com/fwlink/?linkid=191356)

[Get-IscsiTargetPortal](./Get-IscsiTargetPortal.md)
