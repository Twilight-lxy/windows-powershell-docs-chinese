---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/set-iscsitargetserversetting?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IscsiTargetServerSetting
---

# 设置 IscsiTargetServer 的相关参数

## 摘要
用于设置 iSCSI 目标虚拟磁盘的全局配置或通用参数。

## 语法

### IpScoped（默认值）
```
Set-IscsiTargetServerSetting [-IP] <String> [-Port <Int32>] [-Enable <Boolean>] [-PassThru]
 [-ComputerName <String>] [-Credential <PSCredential>] [<CommonParameters>]
```

### ServerGlobal
```
Set-IscsiTargetServerSetting -DisableRemoteManagement <Boolean> [-PassThru] [-ComputerName <String>]
 [-Credential <PSCredential>] [<CommonParameters>]
```

## 描述
`Set-IscsiTargetServerSetting` cmdlet 用于设置 iSCSI 目标的全局配置或通用参数。

## 示例

### 示例 1：设置目标门户端口号
```
PS C:\> Set-IscsiTargetServerSetting -IP 10.1.1.1 -Port 3200
```

这个示例将目标门户的IP地址设置为10.1.1.1，并指定其使用端口编号3200。默认情况下，该门户使用的端口编号是3260。

### 示例 2：禁用目标门户
```
PS C:\> Set-IscsiTargetServerSetting -IP 10.1.1.1 -Enable $False
```

这个示例会禁用目标门户（其IP地址为10.1.1.1）。

### 示例 3：启用目标门户
```
PS C:\> Set-IscsiTargetServerSetting -IP 10.1.1.1 -Port 3200 -Enable $True
```

这个示例使目标门户的IP地址变为10.1.1.1，并将端口号修改为3200。

## 参数

### -ComputerName
如果此 cmdlet 在远程计算机上运行，则会指定远程计算机的名称或 IP 地址。

如果此cmdlet在集群配置上运行，则指定集群资源组的网络名称，或者如果是在集群节点上运行，则指定集群节点的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Credential
指定在连接到远程计算机时的凭据信息。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DisableRemoteManagement
该参数用于指示运行 Microsoft iSCSI Target Server 的计算机是否接受任何基于网络的管理请求。如果您指定值为 $True，那么 iSCSI Target Server 将不会接收那些由包含 SECURITYNETWORK_RID 的线程令牌发出的管理请求。

您只能作为运行 iSCSI 目标服务器的计算机上的本地用户，或者作为拥有 iSCSI 目标服务器集群角色的集群节点来指定此参数。

```yaml
Type: Boolean
Parameter Sets: ServerGlobal
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Enable
指定由用户设置的门户状态。

```yaml
Type: Boolean
Parameter Sets: IpScoped
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -IP
指定一个 IP 地址。

```yaml
Type: String
Parameter Sets: IpScoped
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -Port
指定 iSCSI 目标应监听的端口号。

```yaml
Type: Int32
Parameter Sets: IpScoped
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

### 没有（需要处理的内容）。

## 输出

### Microsoft.Iscsi.Target Commands.IscsiTargetServerSetting

## 备注

## 相关链接

[Set-IscsiTargetServerSetting](./Set-IscsiTargetServerSetting.md)

