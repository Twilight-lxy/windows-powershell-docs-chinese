---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/new-vmreplicationauthorizationentry?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-VMReplicationAuthorizationEntry
---

# 新的虚拟机复制授权条目

## 摘要
创建一个新的授权条目，允许一个或多个主服务器将数据复制到指定的副本服务器上。

## 语法

```
New-VMReplicationAuthorizationEntry [-AllowedPrimaryServer] <String> [-ReplicaStorageLocation] <String>
 [-TrustGroup] <String> [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-VMReplicationAuthorizationEntry` cmdlet 用于创建一个新的授权条目，该条目允许一个或多个主服务器进行数据复制。要使用此 cmdlet，必须确保 Replica 服务器的 `ReplicationAllowedFromAnyServer` 属性的值为 `False`。你可以使用 `Get-VMReplicationServer` cmdlet 来查看该属性的值。

## 示例

#### 示例 1
```
PS C:\> New-VMReplicationAuthorizationEntry server01.domain01.contoso.com D:\ReplicaVMStorage DEFAULT
```

这个示例在本地服务器上为名为 server01.domain01.contoso.com 的主服务器以及名为 DEFAULT 的信任组创建了一个复制授权条目。同时，它还指定了 D:\ReplicaVMStorage 作为用于存储从 server01.domain01.contoso.com 复制的虚拟机所需的复制虚拟硬盘的位置。

### 示例 2
```
PS C:\> New-VMReplicationAuthorizationEntry *.domain01.contoso.com D:\ReplicaVMStorage MyDomain01 -ComputerName server02.domain01.contoso.com
```

这个示例在服务器 server02.domain01.contoso.com 上创建了一个复制授权条目，允许来自 domain01.contoso.com 域内所有属于信任组 MyDomain01 的主服务器的复制操作。同时，它还指定了 D:\ReplicaVMStorage 作为存放从这些被允许的主服务器复制的虚拟机所使用的复制虚拟硬盘的位置。

## 参数

### -AllowedPrimaryServer
指定允许向副本服务器发送复制数据的服务器。仅支持完全限定的域名（fully-qualified domain names）和完全限定的国际域名（fully-qualified international domain names）。您可以在第一个八位字节中使用通配符（例如“*”）来指定一个完全限定的域名，例如 *.contoso.com。

```yaml
Type: String
Parameter Sets: (All)
Aliases: AllowedPS

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如使用[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet生成的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于创建授权条目的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行选择。默认值是本地计算机。可以使用 “localhost” 或句点（.）来明确表示本地计算机。

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

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ReplicaStorageLocation
指定用于存储从允许使用的服务器发送来的副本虚拟硬盘文件的位置，这些文件是在创建新的副本虚拟机时产生的。

```yaml
Type: String
Parameter Sets: (All)
Aliases: StorageLoc

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TrustGroup
该机制用于识别一组主服务器，给定的主虚拟机可以在这些主服务器之间迁移。这样，副本服务器只会接受来自属于该信任组的主服务器的复制请求。你可以使用任意字符串来创建一个新的信任组，并确保某个特定信任组内的所有主服务器都使用你为此参数指定的相同字符串作为标识符。

使用信任组可以帮助您保持虚拟机的隔离状态，因为您可以控制哪些主服务器被允许执行复制操作；同时，这些虚拟机也可以在主服务器之间进行迁移（例如通过实时迁移或从集群节点中进行故障转移）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被运行。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMReplicationAuthorizationEntry

## 备注

## 相关链接

