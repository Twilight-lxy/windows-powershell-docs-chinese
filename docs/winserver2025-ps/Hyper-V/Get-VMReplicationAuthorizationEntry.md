---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmreplicationauthorizationentry?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMReplicationAuthorizationEntry
---

# 获取虚拟机复制授权条目

## 摘要
获取副本服务器的授权配置信息。

## 语法

```
Get-VMReplicationAuthorizationEntry [[-AllowedPrimaryServer] <String>] [-ReplicaStorageLocation <String>]
 [-TrustGroup <String>] [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [<CommonParameters>]
```

## 描述
`Get-VMReplicationAuthorizationEntry` cmdlet 用于获取为副本服务器指定的复制授权信息。

## 示例

### 示例 1
```
PS C:\> Get-VMReplicationAuthorizationEntry
```

这个示例获取了本地复制服务器（Replica server）的复制授权信息（replication authorization entries）。

### 示例 2
```
PS C:\> Get-VMReplicationAuthorizationEntry server01.domain01.contoso.com
```

这个示例获取了名为 server01.domain01.contoso.com 的允许使用的主服务器的复制授权条目。

## 参数

### -AllowedPrimaryServer
指定允许的主服务器，用于从中检索复制授权条目。

```yaml
Type: String
Parameter Sets: (All)
Aliases: AllowedPS

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个或多个用于获取复制授权条目的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址和完全限定域名作为主机标识。默认值为本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

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
当授权的主服务器将复制数据发送到指定的副本服务器时，该选项指定了虚拟硬盘文件存储的位置。

```yaml
Type: String
Parameter Sets: (All)
Aliases: StorageLoc

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TrustGroup
获取那些在 `TrustGroup` 字段中具有指定值的复制授权条目。

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
此cmdlet支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMReplicationAuthorizationEntry

## 备注

## 相关链接

