---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmreplicationauthorizationentry?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMReplicationAuthorizationEntry
---

# Set-VMReplicationAuthorizationEntry

## 摘要
修改副本服务器上的授权条目。

## 语法

### 名称（默认值）
```
Set-VMReplicationAuthorizationEntry [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-AllowedPrimaryServer] <String> [[-ReplicaStorageLocation] <String>]
 [[-TrustGroup] <String>] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 对象
```
Set-VMReplicationAuthorizationEntry [-VMReplicationAuthorizationEntry] <VMReplicationAuthorizationEntry[]>
 [[-ReplicaStorageLocation] <String>] [[-TrustGroup] <String>] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Set-VMReplicationAuthorizationEntry` cmdlet 用于修改复制服务器上的授权条目。

## 示例

#### 示例 1
```
PS C:\> Set-VMReplicationAuthorizationEntry server01.domain01.contoso.com -ReplicaStorageLocation "D:\NewStorageLocation"
```

这个示例将允许的主服务器 server01.domain01.contoso.com 的复制授权条目的位置设置为 D:\NewStorageLocation。

### 示例 2
```
PS C:\> Set-VMReplicationAuthorizationEntry server01.domain01.contoso.com -TrustGroup TrustGroup01
```

此示例将允许的主服务器 server01.domain01.contoso.com 的复制授权条目的信任组设置为 TrustGroup01。

## 参数

### -AllowedPrimaryServer
指定要修改的授权条目中允许使用的主服务器。

```yaml
Type: String
Parameter Sets: Name
Aliases: AllowedPS

Required: True
Position: 0
默认值；常规设置 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。您可以输入一台计算机的名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: Name
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于设置授权条目的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行选择。默认值是本地计算机。可以通过使用 `localhost` 或点号（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: Name
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
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
默认值；常规设置 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: Name
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定一个对象需要被传递给管道系统，该对象代表将要设置的复制授权条目。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicaStorageLocation
指定在新创建副本虚拟机时，用于存储来自允许服务器的副本虚拟硬盘文件的位置。修改此位置不会影响副本服务器上现有的任何虚拟硬盘文件。

```yaml
Type: String
Parameter Sets: (All)
Aliases: StorageLoc

Required: False
Position: 1
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TrustGroup
该参数用于识别一组主服务器，给定的虚拟主机可以移动到这些主服务器中，以确保副本服务器仅从属于该信任组的那些主服务器接收该虚拟主机的复制数据。您可以使用任意字符串来创建一个新的信任组，并确保特定信任组中的所有主服务器都使用与您为此参数指定的值相同的字符串。

使用信任组可以帮助您隔离虚拟机，因为您可以控制哪些主服务器被信任来执行复制操作；同时，虚拟机也可以在不同的主服务器之间迁移（例如通过实时迁移或从集群节点进行故障转移）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMReplicationAuthorizationEntry
指定要设置的授权条目。

```yaml
Type: VMReplicationAuthorizationEntry[]
Parameter Sets: Object
Aliases: VMRepAuthEntry

Required: True
Position: 0
默认值；常规设置 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值；常规设置 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值；常规设置

### VMReplicationAuthorizationEntry
如果指定了 `-PassThru` 参数……

## 备注

## 相关链接

